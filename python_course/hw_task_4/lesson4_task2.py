"""
ЗАДАЧА:
2.	Создайте матрицу 8х8 состоящую из 1 и 0 и заполненную в шахматном порядке
"""
import numpy as np

matrix1 = np.zeros([8,8],int)
matrix1[1::2,::2] = 1
matrix1[::2, 1::2] = 1
print(matrix1)