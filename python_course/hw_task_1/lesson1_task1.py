"""ЗАДАЧА:
# 1)	Напишите функцию которая возвращает длину принимаемой строки, по умолчанию строка пустая (s=’’). Пропишите все аннотации."""


def string_length(s=''):
#функция возвращает длину строки s
    return len(s)

#вызов с пустой строкой
print(string_length())

#вызов с не пустой строкой
print(string_length('Hello world'))
