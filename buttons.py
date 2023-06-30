import telebot
from miha import *
from telebot import types
from config import TOKEN
from tasks_while import *
from tasks_for import *
from tasks_int import *
from tasks_float import *
from tasks_str import *
from tasks_tuple import *
from tasks_set import *
from tasks_list import *
from tasks_dict import *
from tasks_json import *
from tasks_csv import *
from tasks_random import *
from tasks_time import *
from tasks_collection import *
from tasks_infunc import *
from tasks_decor import *
from tasks_zam import *
from tasks_recurs import *

bot = telebot.TeleBot(TOKEN)

def python_guide(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    button_1 = types.KeyboardButton('Типы данных')
    button_2 = types.KeyboardButton('Циклы')
    button_3 = types.KeyboardButton('Модули')
    button_4 = types.KeyboardButton('Функции')
    button_5 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4, button_5)
    bot.send_message(message.chat.id, 'Выбери кнопку', reply_markup=markup)

def data_types(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Изменяемые')
    button_2 = types.KeyboardButton('Неизменяемые')
    button_3 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Выбери кнопку', reply_markup=markup)

def cycle (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Цикл FOR')
    button_2 = types.KeyboardButton('Цикл WHILE')
    button_3 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Выбери кнопку', reply_markup=markup)

def cycle_for (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Описание цикла For')
    button_2 = types.KeyboardButton('Примеры цикла For')
    button_3 = types.KeyboardButton('Задачи цикла For')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери кнопку', reply_markup=markup)

def cycle_while (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Описание цикла While')
    button_2 = types.KeyboardButton('Примеры цикла While')
    button_3 = types.KeyboardButton('Задачи цикла While')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери кнопку', reply_markup=markup)

def tasks_while(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача while 1')
    button_2 = types.KeyboardButton('Задача while 2')
    button_3 = types.KeyboardButton('Задача while 3')
    button_4 = types.KeyboardButton('Задача while 4')
    button_5 = types.KeyboardButton('Задача while 5')
    button_6 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4, button_5, button_6)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_while_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи while 1')
    button_2 = types.KeyboardButton('Назад к задачам while')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, while_task_1, reply_markup=markup)

def tasks_while_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи while 2')
    button_2 = types.KeyboardButton('Назад к задачам while')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, while_task_2, reply_markup=markup)

def tasks_while_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи while 3')
    button_2 = types.KeyboardButton('Назад к задачам while')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, while_task_3, reply_markup=markup)
    
def tasks_while_4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи while 4')
    button_2 = types.KeyboardButton('Назад к задачам while')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, while_task_4, reply_markup=markup)

def tasks_while_5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи while 5')
    button_2 = types.KeyboardButton('Назад к задачам while')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, while_task_5, reply_markup=markup)

def tasks_for(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача for 1')
    button_2 = types.KeyboardButton('Задача for 2')
    button_3 = types.KeyboardButton('Задача for 3')
    button_4 = types.KeyboardButton('Задача for 4')
    button_5 = types.KeyboardButton('Задача for 5')
    button_6 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4, button_5, button_6)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_for_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи for 1')
    button_2 = types.KeyboardButton('Назад к задачам for')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, for_task_1, reply_markup=markup)

def tasks_for_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи for 2')
    button_2 = types.KeyboardButton('Назад к задачам for')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, for_task_2, reply_markup=markup)

def tasks_for_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи for 3')
    button_2 = types.KeyboardButton('Назад к задачам for')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, for_task_3, reply_markup=markup)
    
def tasks_for_4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи for 4')
    button_2 = types.KeyboardButton('Назад к задачам for')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, for_task_4, reply_markup=markup)

def tasks_for_5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи for 5')
    button_2 = types.KeyboardButton('Назад к задачам for')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, for_task_5, reply_markup=markup)

def find_job(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Junior')
    button_2 = types.KeyboardButton('Midle')
    button_3 = types.KeyboardButton('Senior')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Какую должность вы ищите?', reply_markup=markup)

def tasks_int(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача int 1')
    button_2 = types.KeyboardButton('Задача int 2')
    button_3 = types.KeyboardButton('Задача int 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_int_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи int 1')
    button_2 = types.KeyboardButton('Назад к задачам int')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, int_task_1, reply_markup=markup)

def tasks_int_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи int 2')
    button_2 = types.KeyboardButton('Назад к задачам int')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, int_task_2, reply_markup=markup)

def tasks_int_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи int 3')
    button_2 = types.KeyboardButton('Назад к задачам int')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, int_task_3, reply_markup=markup)

def tasks_float(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача float 1')
    button_2 = types.KeyboardButton('Задача float 2')
    button_3 = types.KeyboardButton('Задача float 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_float_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи float 1')
    button_2 = types.KeyboardButton('Назад к задачам float')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, float_task_1, reply_markup=markup)

def tasks_float_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи float 2')
    button_2 = types.KeyboardButton('Назад к задачам float')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, float_task_2, reply_markup=markup)

def tasks_float_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи float 3')
    button_2 = types.KeyboardButton('Назад к задачам float')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, float_task_3, reply_markup=markup)

def tasks_str(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача str 1')
    button_2 = types.KeyboardButton('Задача str 2')
    button_3 = types.KeyboardButton('Задача str 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_str_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи str 1')
    button_2 = types.KeyboardButton('Назад к задачам str')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, str_task_1, reply_markup=markup)

def tasks_str_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи str 2')
    button_2 = types.KeyboardButton('Назад к задачам str')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, str_task_2, reply_markup=markup)

def tasks_str_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи str 3')
    button_2 = types.KeyboardButton('Назад к задачам str')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, str_task_3, reply_markup=markup)

def tasks_tuple(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача tuple 1')
    button_2 = types.KeyboardButton('Задача tuple 2')
    button_3 = types.KeyboardButton('Задача tuple 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_tuple_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи tuple 1')
    button_2 = types.KeyboardButton('Назад к задачам tuple')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, tuple_task_1, reply_markup=markup)

def tasks_tuple_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи tuple 2')
    button_2 = types.KeyboardButton('Назад к задачам tuple')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, tuple_task_2, reply_markup=markup)

def tasks_tuple_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи tuple 3')
    button_2 = types.KeyboardButton('Назад к задачам tuple')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, tuple_task_3, reply_markup=markup)

def tasks_set(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача set 1')
    button_2 = types.KeyboardButton('Задача set 2')
    button_3 = types.KeyboardButton('Задача set 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_set_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи set 1')
    button_2 = types.KeyboardButton('Назад к задачам set')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, set_task_1, reply_markup=markup)

def tasks_set_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи set 2')
    button_2 = types.KeyboardButton('Назад к задачам set')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, set_task_2, reply_markup=markup)

def tasks_set_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи set 3')
    button_2 = types.KeyboardButton('Назад к задачам set')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, set_task_3, reply_markup=markup)

def tasks_list(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача list 1')
    button_2 = types.KeyboardButton('Задача list 2')
    button_3 = types.KeyboardButton('Задача list 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_list_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи list 1')
    button_2 = types.KeyboardButton('Назад к задачам list')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, list_task_1, reply_markup=markup)

def tasks_list_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи list 2')
    button_2 = types.KeyboardButton('Назад к задачам list')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, list_task_2, reply_markup=markup)

def tasks_list_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи list 3')
    button_2 = types.KeyboardButton('Назад к задачам list')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, list_task_3, reply_markup=markup)

def tasks_dict(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача dict 1')
    button_2 = types.KeyboardButton('Задача dict 2')
    button_3 = types.KeyboardButton('Задача dict 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_dict_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи dict 1')
    button_2 = types.KeyboardButton('Назад к задачам dict')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, dict_task_1, reply_markup=markup)

def tasks_dict_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи dict 2')
    button_2 = types.KeyboardButton('Назад к задачам dict')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, dict_task_2, reply_markup=markup)

def tasks_dict_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи dict 3')
    button_2 = types.KeyboardButton('Назад к задачам dict')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, dict_task_3, reply_markup=markup)

def menu1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Json')
    button_2 = types.KeyboardButton('CSV')
    button_3 = types.KeyboardButton('Random')
    button_4 = types.KeyboardButton('Time')
    button_5 = types.KeyboardButton('Collections')
    button_6 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3,button_4,button_5, button_6)
    bot.send_message(message.chat.id, 'Выбери категорию', reply_markup=markup)
def menu2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton('Вложенные функции')
    button_2 = types.KeyboardButton('Декораторы')
    button_3 = types.KeyboardButton('Замыкание')
    button_4 = types.KeyboardButton(' Рекурсивная функция')
    button_5 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3,button_4, button_5)
    bot.send_message(message.chat.id, 'Выбери категорию', reply_markup=markup)

def go_to_site_json(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://pythonworld.ru/moduli/modul-json.html")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по модулю Json', reply_markup=keyboard)

def go_to_site_CSV(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://pythonworld.ru/moduli/modul-csv.html")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по модулю SCV', reply_markup=keyboard)

def go_to_site_Time(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://docs-python.ru/standart-library/modul-time-python/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по модулю Time', reply_markup=keyboard)

def go_to_site_Random(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://pythonworld.ru/moduli/modul-random.html")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по модулю Random', reply_markup=keyboard)

def go_to_site_Collections(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://pythonworld.ru/moduli/modul-collections.html")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по модулю Collections', reply_markup=keyboard)

def go_to_site_vlog(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://www.bestprog.net/ru/2020/08/12/python-nested-functions-nested-scopes-name-search-rules-in-case-of-nested-functions-factory-functions-passing-values-to-a-nested-function-ru/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по вложенным функциям', reply_markup=keyboard)

def go_to_site_dekor(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://pythonworld.ru/osnovy/dekoratory.html")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по декоратору', reply_markup=keyboard)

def go_to_site_zam(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://metanit.com/python/tutorial/2.19.php")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по замыканию', reply_markup=keyboard)

def go_to_site_rekur(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://pythonru.com/osnovy/rekursiya-python")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по рекурсивной функции', reply_markup=keyboard)

def menu_Json():
    return button('Что это?',"Поподробнее","Задачки",'В главное меню')
def menu_CSV():
    return button('Что этo?',"Поподробнеe","Задaчки CSV",'В главное меню')
def menu_Time():
    return button('Чтo этo?',"Поподробнee","Зaдaчки Time",'В главное меню')
def menu_Random():
    return button('Чтo же этo?',"Поподрoбнee","Зaдачки Random",'В главное меню')
def menu_Collections():
    return button('Чтo жe этo?',"Попoдрoбнee","Задачи collection",'В главное меню')

def menu_vlog():
    return button('Описание',"Хочу подробнее","Задания",'В главное меню')
def menu_Dekor():
    return button('Описаниe',"Хочу подробнеe","Задaния",'В главное меню')
def menu_Zam():
    return button('Описaниe',"Хочу подробнee","Зaдaния",'В главное меню')
def menu_rekur():
    return button('Oписaниe',"Хочу подрoбнee","Зaдания",'В главное меню')

def tasks_json(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача json 1')
    button_2 = types.KeyboardButton('Задача json 2')
    button_3 = types.KeyboardButton('Задача json 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_json_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи json 1')
    button_2 = types.KeyboardButton('Назад к задачам json')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, json_task_1, reply_markup=markup)

def tasks_json_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи json 2')
    button_2 = types.KeyboardButton('Назад к задачам json')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, json_task_2, reply_markup=markup)

def tasks_json_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи json 3')
    button_2 = types.KeyboardButton('Назад к задачам json')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, json_task_3, reply_markup=markup)

def tasks_csv(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача csv 1')
    button_2 = types.KeyboardButton('Задача csv 2')
    button_3 = types.KeyboardButton('Задача csv 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_csv_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи csv 1')
    button_2 = types.KeyboardButton('Назад к задачам csv')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, csv_task_1, reply_markup=markup)

def tasks_csv_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи csv 2')
    button_2 = types.KeyboardButton('Назад к задачам csv')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, csv_task_2, reply_markup=markup)

def tasks_csv_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи csv 3')
    button_2 = types.KeyboardButton('Назад к задачам csv')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, csv_task_3, reply_markup=markup)

def tasks_random(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача random 1')
    button_2 = types.KeyboardButton('Задача random 2')
    button_3 = types.KeyboardButton('Задача random 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_random_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи random 1')
    button_2 = types.KeyboardButton('Назад к задачам random')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, random_task_1, reply_markup=markup)

def tasks_random_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи random 2')
    button_2 = types.KeyboardButton('Назад к задачам random')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, random_task_2, reply_markup=markup)

def tasks_random_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи random 3')
    button_2 = types.KeyboardButton('Назад к задачам random')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, random_task_3, reply_markup=markup)

def tasks_time(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача time 1')
    button_2 = types.KeyboardButton('Задача time 2')
    button_3 = types.KeyboardButton('Задача time 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_time_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи time 1')
    button_2 = types.KeyboardButton('Назад к задачам time')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, time_task_1, reply_markup=markup)

def tasks_time_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи time 2')
    button_2 = types.KeyboardButton('Назад к задачам time')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, time_task_2, reply_markup=markup)

def tasks_time_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи time 3')
    button_2 = types.KeyboardButton('Назад к задачам time')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, time_task_3, reply_markup=markup)

def tasks_collection(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача collection 1')
    button_2 = types.KeyboardButton('Задача collection 2')
    button_3 = types.KeyboardButton('Задача collection 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_collection_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи collection 1')
    button_2 = types.KeyboardButton('Назад к задачам collection')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, collection_task_1, reply_markup=markup)

def tasks_collection_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи collection 2')
    button_2 = types.KeyboardButton('Назад к задачам collection')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, collection_task_2, reply_markup=markup)

def tasks_collection_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи collection 3')
    button_2 = types.KeyboardButton('Назад к задачам collection')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, collection_task_3, reply_markup=markup)

def tasks_incfunck(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача incfunck 1')
    button_2 = types.KeyboardButton('Задача incfunck 2')
    button_3 = types.KeyboardButton('Задача incfunck 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_incfunck_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи incfunck 1')
    button_2 = types.KeyboardButton('Назад к задачам incfunck')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, incfunck_task_1, reply_markup=markup)

def tasks_incfunck_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи incfunck 2')
    button_2 = types.KeyboardButton('Назад к задачам incfunck')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, incfunck_task_2, reply_markup=markup)

def tasks_incfunck_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи incfunck 3')
    button_2 = types.KeyboardButton('Назад к задачам incfunck')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, incfunck_task_3, reply_markup=markup)

def tasks_decor(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача decor 1')
    button_2 = types.KeyboardButton('Задача decor 2')
    button_3 = types.KeyboardButton('Задача decor 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_decor_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи decor 1')
    button_2 = types.KeyboardButton('Назад к задачам decor')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, decor_task_1, reply_markup=markup)

def tasks_decor_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи decor 2')
    button_2 = types.KeyboardButton('Назад к задачам decor')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, decor_task_2, reply_markup=markup)

def tasks_decor_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи decor 3')
    button_2 = types.KeyboardButton('Назад к задачам decor')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, decor_task_3, reply_markup=markup)

def tasks_zam(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача zam 1')
    button_2 = types.KeyboardButton('Задача zam 2')
    button_3 = types.KeyboardButton('Задача zam 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_zam_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи zam 1')
    button_2 = types.KeyboardButton('Назад к задачам zam')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, zam_task_1, reply_markup=markup)

def tasks_zam_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи zam 2')
    button_2 = types.KeyboardButton('Назад к задачам zam')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, zam_task_2, reply_markup=markup)

def tasks_zam_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи zam 3')
    button_2 = types.KeyboardButton('Назад к задачам zam')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, zam_task_3, reply_markup=markup)

def tasks_recurs(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Задача recurs 1')
    button_2 = types.KeyboardButton('Задача recurs 2')
    button_3 = types.KeyboardButton('Задача recurs 3')
    button_4 = types.KeyboardButton('В главное меню')
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, 'Выбери задачу', reply_markup=markup)

def tasks_recurs_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи recurs 1')
    button_2 = types.KeyboardButton('Назад к задачам recurs')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, recurs_task_1, reply_markup=markup)

def tasks_recurs_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи recurs 2')
    button_2 = types.KeyboardButton('Назад к задачам recurs')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, recurs_task_2, reply_markup=markup)

def tasks_recurs_3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('Решение задачи recurs 3')
    button_2 = types.KeyboardButton('Назад к задачам recurs')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, recurs_task_3, reply_markup=markup)

def about_us(message):
    video = open('bot/video.mp4', 'rb')
    bot.send_video(message.chat.id, video)
    video.close()