def sum(input, weight):
    result = 0
    for i in range(3):
        result += input[i] * weight[i]
    return result