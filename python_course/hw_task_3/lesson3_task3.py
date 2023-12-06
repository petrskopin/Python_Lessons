"""
ЗАДАЧА:
3.	доработайте задачу 2
a.	Классы “ученик” и “учитель” должны быть наследованы от класса “человек”.
i.	У каждого человека должны быть атрибуты: ФИО, возраст, пол.

b.	Для классов “Материалы” и “Ученик” добавьте магический метод, для вызова функции len() от объектов классов. Материалы должны возвращать кол-во материалов, ученики кол-во знаний.

c.	добавьте в класс ученика, метод, позволяющий ученику случайно "забывать" какую-нибудь часть своих знаний.
"""

from random import sample
from random import randint

class Person:
    def __init__(self, Name, Age, Sex):
        self.Name = Name
        self.Age = Age
        self.Sex = Sex


class Teacher(Person):
    def __init__(self, Name, Age, Sex):
        self.students = 0
        super().__init__(Name, Age, Sex)

    def teach(self, what_to_teach: str, students: list):
        for student in students:
            student.take(what_to_teach)
            self.students += 1


class Student(Person):
    def __init__(self, Name, Age, Sex):
        self.knowledge = []
        super().__init__(Name, Age, Sex)

    def __len__(self):
        return len(self.knowledge)


    def take(self, knowledge_string):
        self.knowledge.append(knowledge_string)

    def forget(self):
        if self.knowledge:
            del self.knowledge[randint(0, len(self.knowledge))-1]


class EducationalMaterials:
    def __init__(self, *args):
        self.materials = list(args)

    def __len__(self):
        return len(self.materials)


# объект учебных материалов
Book = EducationalMaterials('Python', 'Version Control Systems', 'Relational Database', 'NoSQL databases',
                            'Message Brokers')
# объект учителя
Ivanovna = Teacher("Иванова Анна Ивановна", 30, "female")

# 4 ученика
Students = [Student("Петров Петр Петрович", 25, "male"),
            Student("Николаев Николай Николаевич", 50, "male"),
            Student("Олегов Олег Олегович",60, "male"),
            Student("Оксанова Оксана Оксановна", 40, "female")]

# Обучаем каждому из материалов
for i in range(len(Book.materials)):
    Ivanovna.teach(Book.materials[i], sample(Students, randint(1, len(Students))))

# Проверяем знания и их общее число магическим методом
for student in Students:
    print(student.Name, student.knowledge, len(student))

#Студент 0 забывает одно из своих знаний
Students[0].forget()

#Убеждаемся что забыл:
for student in Students:
    print(student.Name, student.knowledge, len(student))

