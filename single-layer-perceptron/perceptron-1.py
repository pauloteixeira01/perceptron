input = [1, 7, 5]

weight = [0.8, 0.1, 0]

def sum(input, weight):
    result = 0
    for i in range(3):
        result += input[i] * weight[i]
    return result

def stepFunction(sum):
    if(sum >= 1):
        return 1
    return 0

print(stepFunction(sum(input, weight)))