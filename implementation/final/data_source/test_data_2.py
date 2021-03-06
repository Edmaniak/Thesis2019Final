import numpy as np

d1 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 4, 0, 0, 4, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 3, 2, 1, 9],
    [9, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 3, 2, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 5, 0, 1, 9],
    [9, 1, 0, 4, 0, 0, 4, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d2 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 2, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 3, 0, 0, 3, 2, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 3, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 3, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 2, 3, 0, 0, 5, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d3 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 3, 2, 0, 3, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 3, 2, 3, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 3, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 2, 3, 0, 0, 5, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d4 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 5, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 3, 2, 3, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 3, 0, 0, 0, 3, 2, 1, 9],
    [9, 1, 0, 3, 2, 3, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d5 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 4, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 3, 2, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 5, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d6 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 0, 5, 0, 4, 1, 9],
    [9, 1, 0, 2, 3, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 0, 0, 0, 4, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 5, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 2, 3, 0, 0, 0, 0, 4, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 4, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d7 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 2, 3, 0, 3, 2, 3, 0, 1, 9],
    [9, 1, 0, 3, 0, 3, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 3, 2, 3, 0, 0, 4, 1, 9],
    [9, 1, 0, 3, 0, 3, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 2, 3, 0, 3, 2, 3, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 4, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d8 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 4, 0, 4, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 3, 2, 3, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 0, 0, 5, 0, 1, 9],
    [9, 1, 0, 0, 4, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],

]

d9 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 4, 0, 0, 4, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 3, 2, 3, 0, 0, 1, 9],
    [9, 1, 2, 3, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 3, 0, 1, 9],
    [9, 1, 4, 0, 5, 0, 0, 3, 2, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d10 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 2, 0, 4, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 3, 2, 3, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 3, 0, 0, 3, 0, 1, 9],
    [9, 1, 0, 0, 0, 2, 0, 0, 2, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d11 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 4, 0, 0, 0, 4, 0, 0, 4, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 3, 2, 3, 0, 4, 1, 9],
    [9, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 0, 0, 0, 4, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 5, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 0, 0, 0, 4, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d12 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 5, 1, 9],
    [9, 1, 0, 2, 3, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 3, 2, 3, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 4, 0, 3, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 2, 3, 0, 2, 0, 4, 1, 9],
    [9, 1, 4, 0, 3, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 4, 0, 4, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d13 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 5, 0, 0, 0, 5, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 2, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 2, 3, 0, 3, 2, 3, 0, 1, 9],
    [9, 1, 4, 0, 2, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d14 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 4, 0, 4, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 2, 3, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 3, 2, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 5, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 4, 0, 4, 0, 4, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d15 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 4, 0, 4, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 4, 1, 9],
    [9, 1, 4, 0, 0, 3, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 3, 2, 3, 0, 0, 4, 1, 9],
    [9, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 3, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 3, 2, 3, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d16 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 4, 0, 4, 0, 4, 0, 0, 1, 9],
    [9, 1, 0, 0, 3, 0, 0, 0, 3, 0, 1, 9],
    [9, 1, 0, 3, 2, 3, 0, 3, 2, 0, 1, 9],
    [9, 1, 0, 0, 3, 0, 0, 0, 3, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 3, 2, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d17 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 4, 4, 0, 0, 0, 0, 4, 4, 1, 9],
    [9, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 3, 2, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 0, 0, 5, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 4, 0, 0, 0, 5, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 4, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d18 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 4, 4, 1, 9],
    [9, 1, 0, 2, 3, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 3, 2, 3, 0, 4, 1, 9],
    [9, 1, 4, 0, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 0, 0, 3, 0, 1, 9],
    [9, 1, 0, 2, 3, 0, 0, 3, 2, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d19 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 4, 0, 4, 4, 0, 4, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 2, 0, 3, 2, 3, 0, 4, 1, 9],
    [9, 1, 0, 3, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 5, 0, 0, 0, 5, 0, 4, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

d20 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 1, 0, 0, 4, 0, 0, 4, 0, 4, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 2, 3, 0, 2, 3, 0, 0, 1, 9],
    [9, 1, 0, 3, 0, 0, 3, 0, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 4, 1, 9],
    [9, 1, 0, 2, 3, 0, 2, 3, 0, 0, 1, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

data = np.array([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20])
object_symbols = [2, 3, 4, 5]