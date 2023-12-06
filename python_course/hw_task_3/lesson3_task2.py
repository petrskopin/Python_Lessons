"""
ЗАДАЧА:
2.	Напишите программу - виртуальную модель процесса обучения.

В программе должны быть объекты: ученик, учитель, учебные материалы.

У каждого учителя должны быть атрибут:
-	количество обученных учеников
		Для учителя добавьте метод “teach”:
-	Метод принимает строку “название материала” и неизвестное количество учеников.
-	Для каждого ученика вызывается метод “take” из класса ученика с параметром “название материала”.
-	Атрибут учителя “количество обученных учеников” увеличивается на 1.
		У каждого ученика должен быть атрибут “knowledge” - список знаний.
		Для ученика создайте метод “take”
-	метод принимает строку знаний и добавляет ее в список знаний ученика.
		Класс учебных материалов
-	должен принимать любое количество не именованных атрибутов и при инициализации сохранять в один атрибут в виде списка.

Для теста программы:
-	создайте объект по классу материалов. При инициализации передайте 5 строк
-	“Python”
-	“Version Control Systems”
-	“Relational Databases”
-	“NoSQL databases”
-	“Message Brokers”
-	Создайте объект учителя
-	Создайте 4 объекта учеников
-	Проведите занятия по каждому материалу (5 раз вызовите метод teach) с произвольным набором учеников.
-	Выведите на печать знания каждого ученика.
"""

from random import sample
from random import randint


class Teacher:
    def __init__(self):
        self.students = 0

    def teach(self, what_to_teach: str, students: list):
        for student in students:
            student.take(what_to_teach)
            self.students += 1


class Student:
    def __init__(self):
        self.knowledge = []

    def take(self, knowledge_string):
        self.knowledge.append(knowledge_string)


class EducationalMaterials:
    def __init__(self, *args):
        self.materials = list(args)


# объект учебных материалов
Book = EducationalMaterials('Python', 'Version Control Systems', 'Relational Database', 'NoSQL databases',
                            'Message Brokers')
# объект учителя
Ivanovna = Teacher()

# 4 ученика
Students = [Student(), Student(), Student(), Student()]

# Обучаем каждому из материалов
for i in range(len(Book.materials)):
    Ivanovna.teach(Book.materials[i], sample(Students, randint(1, len(Students))))

# Проверяем знания
for student in Students:
    print(student.knowledge)
