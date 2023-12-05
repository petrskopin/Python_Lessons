"""ЗАДАЧА:
4.	Имеются два списка состоящие из произвольных элементов. Напишите функцию которая возвращает пересечение списков (элементы которые встречаются в и там и там)
"""


def find_in_both_lists(list1, list2: list):
    return list(filter(lambda x: x in list1, list2))


a = ['123', 6.0, True, 'abcdef', 5]
b = [567, 5, True, 'abcdef', 99, False, 'no']
print(find_in_both_lists(a, b))

