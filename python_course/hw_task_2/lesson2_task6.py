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

@check_if_int
def price_calculation(price, tax):
    return price * (1 + tax)

@check_if_int
def new_test_function(a):
    return a ** a



print(price_calculation(100, 1))

# uncomment line below to raise exception
# print(price_calculation(100,0.5))


print(new_test_function(3))
