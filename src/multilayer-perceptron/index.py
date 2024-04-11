import numpy as np # type: ignore

def sigmoid(sum):
    return 1 / (1 + np.exp(-sum))

def sigmoidDerivative(sigmoidResult):
    return sigmoidResult * (1 - sigmoidResult) 

inputs = np.array([[0,0], [0, 1], [ 1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])

weight0 = np.array([[-0.424, -0.740, -0.961], [0.358, -0.577, -0.469]])
weight1 = np.array([[-0.017], [-0.893], [0.148]])

times = 100

for time in range(times):
    inputs = inputs

    sumSynapse0 = np.dot(inputs, weight0)
    hiddenLayer = sigmoid(sumSynapse0)

    sumSynapse1 = np.dot(hiddenLayer, weight1)
    output = sigmoid(sumSynapse1)

    errorOutput = outputs - output

    average = np.mean(np.abs(errorOutput))

