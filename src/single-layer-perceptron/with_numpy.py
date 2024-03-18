import numpy as np

from sum import sum_with_dot
from status_from_neuron import status_from_neuron

input = np.array([-1, 7, 5])
weight = np.array([0.8, 0.1, 0])

result = status_from_neuron.statusFromNeuron(sum_with_dot.sum(input, weight))

print(result)