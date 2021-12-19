import numpy as np
import random

print("изначальная матрица: ")
a = np.array(([random.random() for i in range(3)], [random.random() for i in range(3)], [random.random() for i in range(3)]))
print(a)

print("транспонированная: ")
b = a.transpose()
print(b)
