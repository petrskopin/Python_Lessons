"""
ЗАДАЧА:
1.	Создайте вектор размером 10 с рандомными значениями, отсортируйте и выведите в консоль.
"""
import numpy as np

vector1 = np.random.random(10)
print("Сгенерированный случайный массив:", vector1)
vector1_sorted = np.sort(vector1)
print("Отсортированный по возрастанию массив:", vector1_sorted)