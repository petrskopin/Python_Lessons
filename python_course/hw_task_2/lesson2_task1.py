"""ЗАДАЧА:
1.	Имеется строка состоящая из слов. Напишите функцию которая возвращает строку убрав из нее стоп слова. Стоп слова находятся в списке:
a.	[“Python”, “php”, “go”, “C”]
"""


def remove_stop_words(input: str, stop_words: list):
    return " ".join(filter(lambda x: x not in stop_words, input.split()))


stop_words = ["Python", "php", "go", "C"]
print(remove_stop_words('This is not php not go not C', stop_words))


