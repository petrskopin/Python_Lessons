"""
ЗАДАЧА:
1.	Создайте матрицы 8x4 и 4x2 и перемножьте, результирующую матрицу выведите в консоль.
"""
import numpy as np
matrix1 = np.ones([8,4])
matrix2 = np.ones([4,2])
matrix3 = np.dot(matrix1,matrix2)
print(matrix3)
