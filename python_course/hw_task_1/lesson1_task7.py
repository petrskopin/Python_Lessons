"""ЗАДАЧА:
7)	* Функция на вход получает 2 переменные.
a)	Кол-во лет (int)
b)	Кол-во месяцев (int)
Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
"""

def count_days(years=0, months=0):
    return (years*12+months)*29

print(count_days(1,1))

