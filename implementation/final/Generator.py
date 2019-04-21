import numpy as np
import matplotlib.pyplot as plt
from keras.engine.saving import model_from_json
import random
import uuid

from implementation.final.Visualiser import Visualiser


class Generator:
    def __init__(self, data_folder, unique_objects_with_symbols=None):
        self.unique_objects_with_symbols = unique_objects_with_symbols
        self.data_folder = data_folder
        self.visualiser = Visualiser()

    def generate_one(self, object_class, default_space, convolutional_cores, random_choice=False, min_probability=0,
                     prediction_map="mul", visualise=None, visualise_save=False):
        return self.generate(default_space, 1, convolutional_cores, random_choice, min_probability, prediction_map,
                             object_class, visualise, visualise_save)

    def generate(self, default_space, iterations, convolutional_cores, random_choice=False, min_probability=0,
                 prediction_map="mul", object_class=None, visualise=None, visualise_save=False):
        default_space = np.array(default_space, int)
        for i_i in range(0, iterations):

            if object_class is None:
                print("Add object:")
                random_class = input()
            else:
                random_class = object_class

            probability_predictions = []

            # LOAD MODEL AND MAKE PREDICTION FOR EACH CORE SNIPPET
            for core_i in range(0, len(convolutional_cores)):

                probability_space = np.zeros((default_space.shape[0], default_space.shape[1]))
                probability_space_width = probability_space.shape[0]
                probability_space_height = probability_space.shape[1]
                probability_space_size = probability_space.shape[0] * probability_space.shape[1]

                core_width = convolutional_cores[core_i][1]
                core_height = convolutional_cores[core_i][0]

                model = self.load_model(random_class, core_width, core_height)
                original_space = np.copy(default_space)

                for c_y in range(0, probability_space_height - core_height + 1):
                    for c_x in range(0, probability_space_width - core_width + 1):
                        to_predict = []
                        for x in range(0, core_width):
                            for y in range(0, core_height):
                                to_predict.append(default_space[x + c_x][y + c_y])

                        # Predicting
                        to_predict = self.spread_objects_to_vector(to_predict, (core_width, core_height))
                        prediction = model.predict(np.reshape(to_predict, (1, to_predict.shape[0])))

                        # Updating the probability space
                        prediction = np.reshape(prediction, (core_width, core_height))
                        for x in range(0, core_height):
                            for y in range(0, core_width):
                                if prediction[x][y] > min_probability:
                                    probability_space[x + c_x][y + c_y] += prediction[x][y]

                # Adding the prediction for specific core
                print("core " + str((core_i + 1)) + " / " + str(len(convolutional_cores)) + " done")
                probability_predictions.append(probability_space)

            final_prediction_mul = probability_predictions[0]
            final_prediction_sum = probability_predictions[0]

            for i in range(1, len(probability_predictions)):
                final_prediction_mul = np.multiply(final_prediction_mul, probability_predictions[i])
                final_prediction_sum = np.add(final_prediction_sum, probability_predictions[i])

            # Choosing the final prediction map
            final_map = final_prediction_sum
            if prediction_map == "sum":
                final_map = final_prediction_sum
            if prediction_map == "mul":
                final_map = final_prediction_mul

            # Normalizing
            max = np.max(final_prediction_sum)
            final_prediction_sum_viz = np.divide(final_prediction_sum, max)
            max = np.max(final_prediction_mul)
            final_prediction_mul_viz = np.divide(final_prediction_mul, max)

            # choosing the final position
            sorted_probability_space = -np.sort(-np.reshape(final_map, (1, probability_space_size)))
            candidate_i = 0
            if random_choice:
                candidate_i = self.pick_random_candidate(sorted_probability_space)
            candidate = sorted_probability_space[0][candidate_i]
            obj_coords = np.where(final_map == candidate)

            while default_space[obj_coords[0][0]][obj_coords[1][0]] > 1:
                candidate_i += 1
                candidate = sorted_probability_space[0][candidate_i]
                obj_coords = np.where(final_map == candidate)

            obj_coords = np.where(final_map == candidate)
            default_space[obj_coords[0][0]][obj_coords[1][0]] = random_class

            if object_class is not None:
                if visualise == "probabilities" or visualise == "both":
                    self.visualiser.visualise_probabilities(final_prediction_sum_viz, visualise_save)
                    self.visualiser.visualise_probabilities(final_prediction_mul_viz, visualise_save)
                if visualise == "result" or visualise == "both":
                    self.visualiser.visualise_space(default_space)
                return default_space

            if visualise is not None:
                images = []
                for prediction_i in range(0, len(probability_predictions)):
                    images.append(probability_predictions[prediction_i])

                columns = 3
                rows = 2

                ax = []
                fig = plt.figure()

                for i in range(columns * rows):
                    ax.append(fig.add_subplot(rows, columns, i + 1))
                    core_i = i + 3
                    ax[-1].set_title("( " + str(core_i) + " x " + str(core_i) + " )")  # set title
                    if i < len(images):
                        plt.imshow(images[i])

                plt.show()
                plt.savefig("results/" + str(uuid.uuid4()) + ".png")

            if visualise == "result":
                self.visualiser.visualise_space(default_space)

            plt.imshow(final_prediction_mul_viz)
            plt.colorbar()
            plt.title("Soucinova matice pravdepodobnosti vyskytu")
            plt.show()

            plt.imshow(final_prediction_sum_viz)
            plt.colorbar()
            plt.title("Souctova matice pravdepodobnosti vyskytu")
            plt.show()

    def pick_random_candidate(self, possibilities):
        sum = int(np.sum(possibilities))
        rand = random.randint(0, sum)
        for i_p in range(0, possibilities.size):
            rand -= possibilities[0][i_p]
            if rand < possibilities[0][i_p]:
                return i_p

    def spread_objects_to_vector(self, data, core_shape):
        vector_size = core_shape[0] * core_shape[1] * self.unique_objects_with_symbols.size
        vector = np.zeros(vector_size, int)
        for i in range(0, len(data)):
            # Floor
            # if data[i] != 0:
            offset = np.where(self.unique_objects_with_symbols == data[i])[0][0]
            object_position = (i * self.unique_objects_with_symbols.size) + offset
            vector[object_position] = 1
        return np.array(vector)

    def load_model(self, object_class, core_width, core_height):
        file_name = "class" + str(object_class) + str(core_width) + str(core_height)
        json_file = open('networks/' + self.data_folder + "/" + file_name + '.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights('networks/' + self.data_folder + "/" + file_name + '.h5')
        return loaded_model

    def test_prediction(self, x, object_class, core_width, core_height):
        core = (len(x), len(x))
        model = self.load_model(object_class, core_width, core_height)
        # Predicting
        prediction = model.predict(np.reshape(x, (1, x.size)))
        # Updating the probability space
        prediction = np.reshape(prediction, (core[0], core[1]))
        print(np.round(prediction, 2))
        return prediction
