# One statistical record for training
class StatisticalRecord:
    def __init__(self, core, object_class, accuracy=0, example_accuracy=0):
        self.core = core,
        self.object_class = object_class
        self.accuracy = accuracy
        self.example_accuracy = example_accuracy


# Class for agregating statistics for NN training
class TrainingStatistics:
    def __init__(self, convolution_cores=[], object_classes=[]):
        self.history_accuracy = []
        self.convolution_cores = convolution_cores
        self.object_classes = object_classes

    def add_core_class(self, record: StatisticalRecord, accuracy=None, example_accuracy=None):
        if accuracy is not None:
            record.accuracy = accuracy
        if example_accuracy is not None:
            record.example_accuracy = example_accuracy
        self.history_accuracy.append(record)

    def get_average_accuracy(self):
        total_sum = 0
        for record_i in range(0, len(self.history_accuracy)):
            total_sum += self.history_accuracy[record_i].accuracy
        return total_sum / len(self.history_accuracy)

    def get_average_example_accuracy(self):
        total_sum = 0
        for record_i in range(0, len(self.history_accuracy)):
            total_sum += self.history_accuracy[record_i].example_accuracy
        return total_sum / len(self.history_accuracy)

    def print_summary(self):
        average = self.get_average_accuracy()
        example_average = self.get_average_example_accuracy()
        for record in self.history_accuracy:
            print(
                "CORE: " + self.get_convolution_core_by_key(
                    record.core[0]) + " | Class: " + self.get_object_class_by_key(
                    record.object_class) + " ===> " + str(record.accuracy) + ", on tested data: " + str(
                    record.example_accuracy))
        print("AVERAGE: " + str(average) + ", ON TESTED: " + str(example_average))

    def get_convolution_core_by_key(self, index):
        return str(self.convolution_cores[index][0])

    def get_object_class_by_key(self, index):
        return str(self.object_classes[index])
