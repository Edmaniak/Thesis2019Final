from implementation.final.DataPreparator import DataPreparator
from implementation.final.Visualiser import Visualiser
from implementation.final.Generator import Generator
from implementation.final.data_source.test_data_3 import data
import numpy as np

cores = [(3, 3), (4, 4), (5, 5), (6, 6)]

special_symbols = (0, 1, 9)
all_object_symbols = np.array([0, 1, 2, 3, 4, 5, 6, 9])
symbols_to_train = [2, 3, 4, 5, 6]

# Tuplets form (rows, columns)
preparator = DataPreparator(data, "finalni", "finalni", symbols_to_train, all_object_symbols, cores,
                            special_symbols)
preparator.prepare_and_fit(50)
visualiser = Visualiser()

default_space = np.array([
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
], int)

visualiser.visualise_space(default_space)

generator = Generator("integracni", all_object_symbols)
generator.generate(default_space, 30, [(3, 3), (4, 4), (5, 5), (6, 6)], 0, "mul",visualise="result")
