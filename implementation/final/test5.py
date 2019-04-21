import numpy as np

from implementation.final.Generator import Generator

# Testujeme zidle kolem stolu
from implementation.final.Visualiser import Visualiser

z = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 3, 2, 3, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

unique_object_with_symbols = np.array([0, 1, 2, 3, 4, 5, 6, 9])
convolutional_cores = [(3, 3), (4, 4), (5, 5), (6, 6)]

generator = Generator("finalni", unique_object_with_symbols)
visualiser = Visualiser()

test_space = np.copy(z)
test_space = generator.generate_one(5, test_space, convolutional_cores, True, visualise="probabilities")
visualiser.visualise_space(test_space, legend=False)
