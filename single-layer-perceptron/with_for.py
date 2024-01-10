from sum import sum
from status_from_neuron import status_from_neuron

input = [1, 7, 5]
weight = [0.8, 0.1, 0]

result = status_from_neuron.statusFromNeuron(sum.sum(input, weight))

print(result)