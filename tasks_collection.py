collection_task_1 = '''Дан список ['apple', 'banana', 'apple', 'banana', 'banana', 'cherry']. Посчитайте количество каждого фрукта в списке.'''
collection_task_1_r = '''
from collections import Counter

fruits = ['apple', 'banana', 'apple', 'banana', 'banana', 'cherry']
fruit_counter = Counter(fruits)

print(fruit_counter)  # Вывод: Counter({'banana': 3, 'apple': 2, 'cherry': 1})
'''
collection_task_2 = 'Создайте словарь, который по умолчанию присваивает значение 0 для несуществующих ключей.'
collection_task_2_r = '''
from collections import defaultdict

default_dict = defaultdict(int)
default_dict['key1'] += 1

print(default_dict)  # Вывод: defaultdict(<class 'int'>, {'key1': 1})
'''
collection_task_3 = 'Создайте очередь с использованием deque и выполните операции "добавить в начало", "добавить в конец", "удалить из начала" и "удалить из конца".'
collection_task_3_r = '''
from collections import deque

# Создание deque
d = deque()

# Добавление в конец
d.append('b')
d.append('c')

# Добавление в начало
d.appendleft('a')

print(d)  # Вывод: deque(['a', 'b', 'c'])

# Удаление из конца
d.pop()

print(d)  # Вывод: deque(['a', 'b'])

# Удаление из начала
d.popleft()

print(d)  # Вывод: deque(['b'])
'''