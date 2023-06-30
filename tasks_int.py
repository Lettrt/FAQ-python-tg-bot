int_task_1 = 'Дана строка, которая представляет собой число. Необходимо преобразовать эту строку в целое число.'
int_task_1_r = '''
s = '12345'
num = int(s)
print(num)
'''
int_task_2 = 'Дано целое число. Необходимо вычислить сумму его цифр.'
int_task_2_r = '''
num = 12345
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print(sum)
'''
int_task_3 = 'Дано целое число. Необходимо определить количество цифр в этом числе.'
int_task_3_r = '''
num = 12345
count = len(str(num))
print(count)
'''