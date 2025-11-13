
import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)
print("matrix:\n", matrix)
diagonal = np.diag(matrix)
print("diagonal element:", diagonal)
total = ("sum of diagonal elements :",diagonal)

total = diagonal.sum()
print("sum of total diagonal :",total)
                              