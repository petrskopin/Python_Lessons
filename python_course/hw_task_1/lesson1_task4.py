"""ЗАДАЧА:
4)	напишите функцию которая
a)	принимает число
b)	Если число больше 100 или меньше -100, то вывести в консоль символ “-”, иначе вывести на экран символ “+”
"""


def check_value(value=0):
    if value > 100 or value < -100:
        print('-')
    else:
        print('+')


check_value(-1550)
check_value(50)
