json_task_1 = 'У вас есть словарь Python и вы хотите преобразовать его в строку JSON.'
json_task_1_r = '''
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(data)
print(json_data)
'''
json_task_2 = 'У вас есть строка JSON, и вы хотите преобразовать её в словарь Python.'
json_task_2_r = '''
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)
'''
json_task_3 = ' вас есть файл data.json, содержащий данные в формате JSON. Прочтите этот файл и преобразуйте его содержимое в словарь Python.'
json_task_3_r = '''
import json

with open('data.json') as f:
    data = json.load(f)

print(data)
'''