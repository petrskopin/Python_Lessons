"""ЗАДАЧА:
3)	Напишите функцию которая:
a)	принимает список с произвольными значениями
b)	добавляет к нему произвольное значение
c)	возвращает результирующий список
"""

def update_list_with_random_value (input=[]):
    input.append("updated")
    return input

print(update_list_with_random_value(['a','b','c']))