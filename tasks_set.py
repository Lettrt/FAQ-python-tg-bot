set_task_1 = 'Создайте множество с несколькими элементами, а затем добавьте в него новый элемент.'
set_task_1_r = '''
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)
'''
set_task_2 = 'Дано множество. Удалите из него элемент, если он присутствует, и выведите получившееся множество.'
set_task_2_r = '''
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)
'''
set_task_3 = 'Даны два множества. Найдите их пересечение.'
set_task_3_r = '''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print(intersection)
'''