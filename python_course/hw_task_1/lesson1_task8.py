"""ЗАДАЧА:
8)	* Напишите функцию которая
a)	на вход получает строковую переменную.
i)	в строке содержится несколько слов
b)	Возвращает строку состоящую из аббревиатур слов переменной.
c)	Если на вход поступил другой тип данных, должно срабатывать исключение
d)	Результат работы функции распечатайте в консоль
"""


def get_first_chars(input_string):
    if type(input_string) == str:
        # мне не нравится решение с поиском первых  слов, но ничего проще я не придумал. Если можно как-то лучше сделать, напишите пожалуйста
        return "".join(word[0] for word in input_string.split(' '))
    else:
        raise Exception("Not a string")


print(get_first_chars("Just a TEST string"))