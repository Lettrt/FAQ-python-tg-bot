incfunck_task_1 = '''Создайте функцию make_multiplier, которая принимает число и возвращает новую функцию, умножающую входные значения на это число.'''
incfunck_task_1_r = '''
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplier_by_2 = make_multiplier(2)
print(multiplier_by_2(5))  # Вывод: 10
'''
incfunck_task_2 = 'Создайте функцию make_power, которая возвращает функцию возведения в степень, используя число из области видимости внешней функции.'
incfunck_task_2_r = '''
def make_power(n):
    def power(x):
        return x ** n
    return power

square = make_power(2)
print(square(5))  # Вывод: 25
'''
incfunck_task_3 = ' Создайте и сразу вызовите функцию, которая выводит "Hello, World!".'
incfunck_task_3_r = '''
(lambda: print("Hello, World!"))()  # Вывод: Hello, World!
'''