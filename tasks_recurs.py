recurs_task_1 = 'Напишите рекурсивную функцию, которая вычисляет факториал числа.'
recurs_task_1_r = '''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
'''
recurs_task_2 = 'Напишите рекурсивную функцию, которая вычисляет n-е число в последовательности Фибоначчи.'
recurs_task_2_r = '''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55
'''
recurs_task_3 = 'Напишите рекурсивную функцию, которая переворачивает строку.'
recurs_task_3_r = '''
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("Hello, World!"))  # Output: "!dlroW ,olleH"
'''