"""ЗАДАЧА:
3.	Напишите функцию, которая принимает любое количество не именованных аргументов и возвращает кортеж состоящий из аргументов у которых тип данных str
"""


def return_only_strings(*args):
    return tuple(filter(lambda x: isinstance(x, str), args))


print(return_only_strings(1,'abc',[1,2,3],'def',5,6.0))