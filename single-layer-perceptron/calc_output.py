from status_from_neuron import status_from_neuron

def calcOutput(register, weights):
    result = register.dot(weights)
    return status_from_neuron.statusFromNeuron(result)