decor_task_1 = 'Создайте декоратор log, который записывает в консоль имя вызываемой функции и ее аргументы.'
decor_task_1_r = '''
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Вызывается функция {func.__name__} с аргументами {args} и ключевыми аргументами {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(x, y):
    return x + y

print(add(5, 3))
'''
decor_task_2 = 'Создайте декоратор timeit, который измеряет и выводит время выполнения функции.'
decor_task_2_r = '''
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция {func.__name__} выполнена за {end - start} секунд")
        return result
    return wrapper

@timeit
def squares(n):
    return [i ** 2 for i in range(n)]

print(squares(1000000))
'''
decor_task_3 = 'Создайте декоратор memoize, который сохраняет результаты предыдущих вызовов функции и возвращает сохраненный результат, когда функция вызывается с теми же аргументами.'
decor_task_3_r = '''
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))
'''