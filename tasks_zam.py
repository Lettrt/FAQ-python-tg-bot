zam_task_1 = 'Создайте замыкание make_counter, которое реализует счетчик: каждый вызов возвращает следующее число..'
zam_task_1_r = '''
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = make_counter()
print(counter())  # Output: 1
print(counter())  # Output: 2
'''
zam_task_2 = 'Создайте замыкание make_accumulator, которое реализует аккумулятор: каждый вызов добавляет аргумент к аккумулированному значению и возвращает его.'
zam_task_2_r = '''
def make_accumulator():
    total = 0
    def accumulator(n):
        nonlocal total
        total += n
        return total
    return accumulator

accumulator = make_accumulator()
print(accumulator(5))  # Output: 5
print(accumulator(6))  # Output: 11
'''
zam_task_3 = 'Создайте замыкание make_multiplier, которое принимает число и возвращает функцию, умножающую свои аргументы на это число.'
zam_task_3_r = '''
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplier_by_2 = make_multiplier(2)
print(multiplier_by_2(7))  # Output: 14

multiplier_by_3 = make_multiplier(3)
print(multiplier_by_3(5))  # Output: 15
'''