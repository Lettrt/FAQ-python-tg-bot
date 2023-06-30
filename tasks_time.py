time_task_1 = 'Необходимо приостановить выполнение программы на случайное количество времени от 1 до 5 секунд.'
time_task_1_r = '''
import time
import random

delay = random.randint(1, 5)
time.sleep(delay)
print(f"Программа приостановлена на {delay} секунд.")
'''
time_task_2 = 'Вывести текущее время каждую случайную секунду в течение 10 секунд.'
time_task_2_r = '''
import time
import random

start_time = time.time()

while time.time() - start_time < 10:
    time.sleep(random.random())
    print("Текущее время:", time.ctime())
'''
time_task_3 = 'Создать список из 5 случайных дат в промежутке между двумя определёнными датами.'
time_task_3_r = '''
import random
import time

start_date = time.mktime(time.strptime("2020-01-01", "%Y-%m-%d"))
end_date = time.mktime(time.strptime("2023-01-01", "%Y-%m-%d"))

random_dates = []

for _ in range(5):
    random_date = random.randint(start_date, end_date)
    date = time.strftime("%Y-%m-%d", time.localtime(random_date))
    random_dates.append(date)

print(random_dates)
'''