from sum import sum
from step_function import step_function

input = [-1, 7, 5]
weight = [0.8, 0.1, 0]

result = step_function.stepFunction(sum.sum(input, weight))

print(result)