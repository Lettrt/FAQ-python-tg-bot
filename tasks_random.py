random_task_1 = 'Необходимо сгенерировать случайное целое число в диапазоне от 1 до 100.'
random_task_1_r = '''
import random

random_number = random.randint(1, 100)
print(random_number)
'''
random_task_2 = 'У вас есть список и вы хотите выбрать случайный элемент из этого списка.'
random_task_2_r = '''
import random

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random_element = random.choice(my_list)
print(random_element)
'''
random_task_3 = ' У вас есть список и вы хотите перемешать его элементы в случайном порядке.'
random_task_3_r = '''
import random

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random.shuffle(my_list)
print(my_list)
'''