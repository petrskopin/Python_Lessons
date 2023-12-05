"""
ЗАДАЧА:
6.	Напишите декоратор который выводит исключение в случае если декорируемая функция возвращает тип данных отличный от int
Напишите 2 тестовые декорируемые функции с произвольными данными.

"""


def check_if_int(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if isinstance(result, int):
            return result
        else:
            raise Exception('Result value is not int')

    return wrapper


def price_calculation(price, tax):
    return price * (1 + tax)


def new_test_function(a):
    return a ** a


price_calculation = check_if_int(price_calculation)
print(price_calculation(100, 1))

# uncomment line below to raise exception
# print(price_calculation(100,0.5))

print(new_test_function(3))
new_test2 = check_if_int(new_test_function)
print(new_test2(3))
