"""
ЗАДАЧА:
7.	Напишите декоратор который запускает декорируемую функцию повторно, в случае если произошло исключение при первом запуске.
Напишите 2 тестовые декорируемые функции с произвольными данными.
"""


def run_it_twice(fn):
    def wrapper(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
        except:
            print("starting second time")
            result = fn(*args, **kwargs)
        return result
    return wrapper


def plus_one(x):
    return x + 1


def divide_by_zero(x):
    return x / 0


plus_one = run_it_twice(plus_one)
print(plus_one(1))
divide_by_zero = run_it_twice(divide_by_zero)
print(divide_by_zero(5))
