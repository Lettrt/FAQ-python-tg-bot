dict_task_1 = 'Создайте словарь, который будет содержать информацию о студенте: имя, возраст и группа. Затем выведите эту информацию.'
dict_task_1_r = '''
student = {
    "name": "Alex",
    "age": 21,
    "group": "Biology"
}
student["grade"] = "A"
print(student)
'''
dict_task_2 = 'Добавьте в словарь студента новый ключ "grade" со значением "A" и выведите обновленный словарь.'
dict_task_2_r = '''
student = {
    "name": "Alex",
    "age": 21,
    "group": "Biology"
}
student["grade"] = "A"
print(student)
'''
dict_task_3 = 'Удалите из словаря студента ключ "age" и выведите обновленный словарь.'
dict_task_3_r = '''
student = {
    "name": "Alex",
    "age": 21,
    "group": "Biology"
}
del student["age"]
print(student)
'''