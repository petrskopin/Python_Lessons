"""ЗАДАЧА:
5)	Напишите функцию которая отвечает “ДА” или “НЕТ” на вопрос в комментарие.
"""


def check_if_substring(string1='', string2=''):
    if string2 in string1:
        print("ДА")
    else:
        print("НЕТ")


str_1 = 'test'
str_2 = 'test1'
# проверяем содержит ли строка test1 в себе строку test
check_if_substring(str_2, str_1)
