import numpy as np

from implementation.final.Generator import Generator

# Testujeme zidle kolem stolu
from implementation.final.Visualiser import Visualiser

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

unique_object_with_symbols = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
convolutional_cores = [(3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]

visualiser = Visualiser()
generator = Generator("integracni", unique_object_with_symbols)
generator.generate(default_space, 20, convolutional_cores, True, 0, visualise="result")
