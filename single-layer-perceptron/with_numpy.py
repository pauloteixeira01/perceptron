import numpy as np

input = np.array([-1, 7, 5])
weight = np.array([0.8, 0.1, 0])

def sum(input, weight):
    return input.dot(weight)

def stepFunction(sum):
    if(sum >= 1):
        return 1
    return 0

print(stepFunction(sum(input, weight)))