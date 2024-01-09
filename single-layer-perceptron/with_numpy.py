import numpy as np

from sum import sum_with_dot
from step_function import step_function

input = np.array([1, 7, 5])
weight = np.array([0.8, 0.1, 0])

result = step_function.stepFunction(sum_with_dot.sum(input, weight))

print(result)