"""ЗАДАЧА:
Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них
"""


def find_positive(values: list):
    count = 0
    for value in values:
        if value > 0:
            count += 1
    return count

print(find_positive([1, 2, -3, 4, -5]))
