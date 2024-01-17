import numpy as np

from status_from_neuron import status_from_neuron

input = np.array([[0,0], [0,1], [1,0], [1,1]])
output = np.array([0, 0, 0, 1])
weights = np.array([0.0, 0.0])
learningRate = 0.1

def calcOutput(register):
    result = register.dot(weights)
    return status_from_neuron.statusFromNeuron(result)

def toTrain():
    return 0