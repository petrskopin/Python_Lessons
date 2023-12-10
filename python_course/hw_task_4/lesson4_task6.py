"""
ЗАДАЧА:
6.	Постройте класс для анализа файла с данными:
a.	Класс принимает путь к файлу при инициализации
b.	Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
Файл состоит из строк с произвольным текстом, элементами массива должны быть строки.
c.	Создайте метод поиска по тексту. Метод принимает паттерн поиска и возвращает список всех найденных совпадений.
"""

import numpy as np
import re

class TextFile:
    def __init__(self, path: str):
        self.path = path

    def readdata(self):
        self.data=[]
        with open(self.path, 'r') as file:
            #построчно записываем в numpy массив data. Зачем в этой задаче numpy правда совсем не понятно
            self.data = np.append(self.data, file.readlines())


    def find_pattern(self, pattern:str):
        result = []
        for string1 in self.data:
            a = re.findall(pattern,string1)
            if a:
                result.append(a)
        return result



File1 = TextFile('test_data.txt')
File1.readdata()
print(File1.find_pattern('\d{4}'))