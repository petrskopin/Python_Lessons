"""
1.	Создайте класс  прямоугольника. Класс принимает два параметра, ширина и высота прямоугольника.
Создайте два метода:
-	метод возвращающий площадь прямоугольника
-	метод возвращающий периметр прямоугольника
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def find_area(self):
        return self.width * self.height

    def find_perimiter(self):
        return (self.width+self.height) * 2


my_new_rectangle = Rectangle(10,5)
print(f'Ширина: {my_new_rectangle.width}, Высота: {my_new_rectangle.height}, Площадь: {my_new_rectangle.find_area()},'
      f' Периметр: {my_new_rectangle.find_perimiter()}')
