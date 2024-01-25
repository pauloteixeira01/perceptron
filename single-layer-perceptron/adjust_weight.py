import numpy as np

from status_from_neuron import status_from_neuron
from to_train import toTrain
from calc_output import calcOutput

# and
# inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
# outputs = np.array([0, 0, 0, 1])

# or
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
outputs = np.array([0, 1, 1, 1])

weights = np.array([0.0, 0.0])
learningRate = 0.1

toTrain(inputs, outputs, weights, learningRate)
print('Neural network trained!')

for outputRegister in range(len(outputs)):
    registers = np.array(inputs[outputRegister])
    print(calcOutput(registers, weights)) 