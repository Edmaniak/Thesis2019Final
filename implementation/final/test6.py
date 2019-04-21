import numpy as np

from implementation.final.Generator import Generator

# Testujeme zidle kolem stolu
from implementation.final.Visualiser import Visualiser

default_space = np.array([
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
])

unique_object_with_symbols = np.array([0, 1, 2, 3, 4, 5, 6, 9])
convolutional_cores = [(3, 3), (4, 4), (5, 5), (6, 6)]

generator = Generator("4", unique_object_with_symbols)

generator = Generator("finalni", unique_object_with_symbols)
visualiser = Visualiser()

test_space = np.copy(default_space)
for j in range(0, 10):
    test_space = np.copy(default_space)
    generator = Generator("finalni", unique_object_with_symbols)
    for i in range(0, 10):
        test_space = generator.generate_one(6, test_space, convolutional_cores, True)
    for i in range(0, 10):
        test_space = generator.generate_one(4, test_space, convolutional_cores, True)
    visualiser.visualise_space(test_space)
