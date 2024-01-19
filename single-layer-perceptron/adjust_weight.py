import numpy as np

from status_from_neuron import status_from_neuron
from to_train import toTrain

inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
outputs = np.array([0, 0, 0, 1])
weights = np.array([0.0, 0.0])
learningRate = 0.1

toTrain(inputs, outputs, weights, learningRate)