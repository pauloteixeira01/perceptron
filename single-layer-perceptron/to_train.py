import numpy as np

from calc_output import calcOutput

def toTrain(inputs, outputs, weights, learningRate):
    totalError = 1
    while(totalError != 0):
        totalError = 0
        for outputRegister in range(len(outputs)):
            calculatedOutputs = calcOutput(np.array(inputs[outputRegister]), weights)
            error = abs(outputs[outputRegister] - calculatedOutputs)
            totalError += error
            for weightRegister in range(len(weights)):
                weights[weightRegister] = weights[weightRegister] + (learningRate * inputs[outputRegister][weightRegister] * error)
                print('Updated weight : ' + str(weights[weightRegister]))
        print('Total errors: ' + str(totalError))