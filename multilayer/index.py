import numpy as np


def sigmoid(sum):
    return 1 / (1 + np.exp(-sum))

a = sigmoid(1.5)

print(a)