csv_task_1 = 'У вас есть CSV файл data.csv и вы хотите прочитать его и вывести данные.'
csv_task_1_r = '''
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''
csv_task_2 = 'У вас есть список, и вы хотите записать его в CSV файл data.csv.'
csv_task_2_r = '''
import csv

data = [['Name', 'Age'], ['John', '20'], ['Doe', '30']]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
'''
csv_task_3 = 'У вас есть CSV файл data.csv и вы хотите прочитать его и сохранить данные в виде словаря.'
csv_task_3_r = '''
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
'''