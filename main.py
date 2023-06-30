import telebot, subprocess
from telebot import types
from config import TOKEN
from buttons import *
from texts import *
from tasks_while import *
from tasks_for import *
from tasks_int import *
from buttons_miha import *
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
from jun import send_june 
from middle import send_middle
from senior import send_senior


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton('FAQ')
    button_2 = types.KeyboardButton('PEP-8')
    button_3 = types.KeyboardButton('Python guide')
    button_4 = types.KeyboardButton('About us')
    button_5 = types.KeyboardButton('Найти работу')
    markup.add(button_1, button_2, button_3, button_4, button_5)

    welcome_text = f'Привет, *{message.from_user.username}*!\n\n' \
                   f'*Чтобы узнать о моих функциях* можешь нажать кнопку FAQ. \n' \
                   f'*Чтобы начать работу* нажми кнопку Menu'
    
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "PEP-8")
def send_pep8(message):
    url = "https://peps.python.org/pep-0008/"
    bot.send_message(message.chat.id, f'[Официальная документация PEP-8]({url})', parse_mode='Markdown')


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == 'Python guide':
        python_guide(message)
    elif message.text == 'В главное меню':
        welcome(message)
    elif message.text == 'Типы данных':
        data_types(message)
    elif message.text == 'Циклы':
        cycle(message)
    elif message.text == 'Цикл FOR':
        cycle_for(message)
    elif message.text == 'Описание цикла For':
        bot.send_message(message.chat.id, discr_for)
    elif message.text == 'Цикл WHILE':
        cycle_while(message)
    elif message.text == 'Описание цикла While':
        bot.send_message(message.chat.id, discr_while)
    elif message.text == 'Примеры цикла While':
        bot.send_message(message.chat.id, discr_while_example)
    elif message.text == 'Задачи цикла While':
        tasks_while(message)
    elif message.text == 'Задача while 1':
        tasks_while_1(message)
    elif message.text == 'Решение задачи while 1':
        bot.send_message(message.chat.id, while_task_1_r)
    elif message.text == 'Задача while 2':
        tasks_while_2(message)
    elif message.text == 'Решение задачи while 2':
        bot.send_message(message.chat.id, while_task_2_r)
    elif message.text == 'Задача while 3':
        tasks_while_3(message)
    elif message.text == 'Решение задачи while 3':
        bot.send_message(message.chat.id, while_task_3_r)
    elif message.text == 'Задача while 4':
        tasks_while_4(message)
    elif message.text == 'Решение задачи while 4':
        bot.send_message(message.chat.id, while_task_4_r)
    elif message.text == 'Задача while 5':
        tasks_while_5(message)
    elif message.text == 'Решение задачи while 5':
        bot.send_message(message.chat.id, while_task_5_r)
    elif message.text == 'Назад к задачам while':
        tasks_while(message)
    elif message.text == 'Задачи цикла For':
        tasks_for(message)
    elif message.text == 'Назад к задачам for':
        tasks_for(message)
    elif message.text == 'Задача for 1':
        tasks_for_1(message)
    elif message.text == 'Решение задачи for 1':
        bot.send_message(message.chat.id, for_task_1_r)
    elif message.text == 'Задача for 2':
        tasks_for_2(message)
    elif message.text == 'Решение задачи for 2':
        bot.send_message(message.chat.id, for_task_2_r)
    elif message.text == 'Задача for 3':
        tasks_for_3(message)
    elif message.text == 'Решение задачи for 3':
        bot.send_message(message.chat.id, for_task_3_r)
    elif message.text == 'Задача for 4':
        tasks_for_4(message)
    elif message.text == 'Решение задачи for 4':
        bot.send_message(message.chat.id, for_task_4_r)
    elif message.text == 'Задача for 5':
        tasks_for_5(message)
    elif message.text == 'Решение задачи for 5':
        bot.send_message(message.chat.id, for_task_5_r)
    elif message.text == 'Найти работу':
        find_job(message)
    elif message.text == 'Определение':
        bot.send_message(message.chat.id, discr_set)
    elif message.text == 'Set':
        bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Set-множество",reply_markup=menu_set()) 
    elif message.text == 'List':
        bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: List-списки",reply_markup=menu_list())
    elif message.text == 'Tuple':
        bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Tuple-кортежи",reply_markup=menu_tuple())
    elif message.text == 'Str':
        bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Str-строки",reply_markup=menu_str())   
    elif message.text == 'Определениe':
        bot.send_message(message.chat.id,discr_list) 
    elif message.text == 'Dictionary':
        bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Dictionary-словари",reply_markup=menu_dictionary())   
    elif message.text == 'Int':
        bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Integer",reply_markup=menu_int())  
    elif message.text == 'Float':
        bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Float",reply_markup=menu_float())
    elif message.text == 'Определениe':
        bot.send_message(message.chat.id,"Это удобный способ хранения данных с возможностью их изменения") 
    elif message.text == 'Определeниe':
        bot.send_message(message.chat.id, discr_tuple) 
    elif message.text == 'Опредeлeниe':
        bot.send_message(message.chat.id,"Это любые данные взятые в ковычки") 
    elif message.text == 'Опрeдeлeниe':
        bot.send_message(message.chat.id, discr_dict) 
    elif message.text == 'Опpeдeлeниe':
        bot.send_message(message.chat.id,discr_int) 
    elif message.text == 'Oпpeдeлeниe':
        bot.send_message(message.chat.id,discr_float) 
    elif message.text == "Подробное описаниe":
        go_to_site_list(message) 
    elif message.text == "Подробноe описаниe":
        go_to_site_tuple(message)
    elif message.text == "Подробное описание":
        go_to_site_set(message)
    elif message.text == "Подробное oписание":
        go_to_site_str(message)
    elif message.text == "Подробнoe oписаниe":
        go_to_site_dictionary(message)
    elif message.text == "Подpобнoe oписаниe":
        go_to_site_int(message)
    elif message.text == "Пoдpобнoe oписаниe":
        go_to_site_float(message)
    elif message.text == "Изменяемые":
        bot.send_message(message.chat.id,"Вы выбрали изменяемые типы данных ",reply_markup=menu_ism())
    elif message.text == "Неизменяемые":
        bot.send_message(message.chat.id,"Вы выбрали неизменяемые типы данных",reply_markup= menu_neism())
    elif message.text=='Возврат к главному меню':
        bot.send_message(message.chat.id,"Сделайте выбор",reply_markup=menu())
    elif message.text == 'Задачa на peшeниe':
        tasks_int(message)
    elif message.text == 'Назад к задачам int':
        tasks_int(message)
    elif message.text == 'Задача int 1':
        tasks_int_1(message)
    elif message.text == 'Решение задачи int 1':
        bot.send_message(message.chat.id, int_task_1_r)
    elif message.text == 'Задача int 2':
        tasks_int_2(message)
    elif message.text == 'Решение задачи int 2':
        bot.send_message(message.chat.id, int_task_2_r)
    elif message.text == 'Задача int 3':
        tasks_int_3(message)
    elif message.text == 'Решение задачи int 3':
        bot.send_message(message.chat.id, int_task_3_r)
    elif message.text == 'Зaдачa на peшeниe':
        tasks_float(message)
    elif message.text == 'Назад к задачам float':
        tasks_float(message)
    elif message.text == 'Задача float 1':
        tasks_float_1(message)
    elif message.text == 'Решение задачи float 1':
        bot.send_message(message.chat.id, float_task_1_r)
    elif message.text == 'Задача float 2':
        tasks_float_2(message)
    elif message.text == 'Решение задачи float 2':
        bot.send_message(message.chat.id, float_task_2_r)
    elif message.text == 'Задача float 3':
        tasks_float_3(message)
    elif message.text == 'Решение задачи float 3':
        bot.send_message(message.chat.id, float_task_3_r)
    elif message.text == 'Задача на рeшeниe':
        tasks_str(message)
    elif message.text == 'Назад к задачам str':
        tasks_str(message)
    elif message.text == 'Задача str 1':
        tasks_str_1(message)
    elif message.text == 'Решение задачи str 1':
        bot.send_message(message.chat.id, str_task_1_r)
    elif message.text == 'Задача str 2':
        tasks_str_2(message)
    elif message.text == 'Решение задачи str 2':
        bot.send_message(message.chat.id, str_task_2_r)
    elif message.text == 'Задача str 3':
        tasks_str_3(message)
    elif message.text == 'Решение задачи str 3':
        bot.send_message(message.chat.id, str_task_3_r)
    elif message.text == 'Задача на решeниe':
        tasks_tuple(message)
    elif message.text == 'Назад к задачам tuple':
        tasks_tuple(message)
    elif message.text == 'Задача tuple 1':
        tasks_tuple_1(message)
    elif message.text == 'Решение задачи tuple 1':
        bot.send_message(message.chat.id, tuple_task_1_r)
    elif message.text == 'Задача tuple 2':
        tasks_tuple_2(message)
    elif message.text == 'Решение задачи tuple 2':
        bot.send_message(message.chat.id, tuple_task_2_r)
    elif message.text == 'Задача tuple 3':
        tasks_tuple_3(message)
    elif message.text == 'Решение задачи tuple 3':
        bot.send_message(message.chat.id, tuple_task_3_r)
    elif message.text == 'Задача на решение':
        tasks_set(message)
    elif message.text == 'Назад к задачам set':
        tasks_set(message)
    elif message.text == 'Задача set 1':
        tasks_set_1(message)
    elif message.text == 'Решение задачи set 1':
        bot.send_message(message.chat.id, set_task_1_r)
    elif message.text == 'Задача set 2':
        tasks_set_2(message)
    elif message.text == 'Решение задачи set 2':
        bot.send_message(message.chat.id, set_task_2_r)
    elif message.text == 'Задача set 3':
        tasks_set_3(message)
    elif message.text == 'Решение задачи set 3':
        bot.send_message(message.chat.id, set_task_3_r)
    elif message.text == 'Задача на решениe':
        tasks_list(message)
    elif message.text == 'Назад к задачам list':
        tasks_list(message)
    elif message.text == 'Задача list 1':
        tasks_list_1(message)
    elif message.text == 'Решение задачи list 1':
        bot.send_message(message.chat.id, list_task_1_r)
    elif message.text == 'Задача list 2':
        tasks_list_2(message)
    elif message.text == 'Решение задачи list 2':
        bot.send_message(message.chat.id, list_task_2_r)
    elif message.text == 'Задача list 3':
        tasks_list_3(message)
    elif message.text == 'Решение задачи list 3':
        bot.send_message(message.chat.id, list_task_3_r)
    elif message.text == 'Задача на peшeниe':
        tasks_dict(message)
    elif message.text == 'Назад к задачам dict':
        tasks_dict(message)
    elif message.text == 'Задача dict 1':
        tasks_dict_1(message)
    elif message.text == 'Решение задачи dict 1':
        bot.send_message(message.chat.id, dict_task_1_r)
    elif message.text == 'Задача dict 2':
        tasks_dict_2(message)
    elif message.text == 'Решение задачи dict 2':
        bot.send_message(message.chat.id, dict_task_2_r)
    elif message.text == 'Задача dict 3':
        tasks_dict_3(message)
    elif message.text == 'Решение задачи dict 3':
        bot.send_message(message.chat.id, dict_task_3_r) 
    elif message.text == 'Модули':
        menu1(message)
    elif message.text == 'Функции':
        menu2(message)
    elif message.text == 'Json':
        bot.send_message(message.chat.id,"Вы выбрали тему-модули: Json",reply_markup=menu_Json()) 
    elif message.text == 'CSV':
        bot.send_message(message.chat.id,"Вы выбрали тему-модули: CSV",reply_markup=menu_CSV()) 
    elif message.text == 'Time':
        bot.send_message(message.chat.id,"Вы выбрали тему-модули: Time",reply_markup=menu_Time()) 
    elif message.text == 'Random':
        bot.send_message(message.chat.id,"Вы выбрали тему-модули: Random",reply_markup=menu_Random()) 
    elif message.text == 'Collections':
        bot.send_message(message.chat.id,"Вы выбрали тему-модули: Collections",reply_markup=menu_Collections()) 
    elif message.text == 'Что это?':
        bot.send_message(message.chat.id,"Json является одним из главных форматов общения компьютеров в сети") 
    elif message.text == 'Что этo?':
        bot.send_message(message.chat.id,"CSV это текстовый формат, предназначенный для представления табличных данных") 
    elif message.text == 'Чтo этo?':
        bot.send_message(message.chat.id,"Модуль Time предоставляет доступ к нескольким различным типам часов, каждый из которых используется для разных целей") 
    elif message.text == 'Чтo же этo?':
        bot.send_message(message.chat.id,"Модуль random предоставляет функции для генерации случайных чисел, букв, случайного выбора элементов последовательности.") 
    elif message.text == 'Чтo жe этo?':
        bot.send_message(message.chat.id,"Модуль collections - предоставляет специализированные типы данных, на основе словарей, кортежей, множеств, списков.") 
    elif message.text == "Поподробнее":
        go_to_site_json(message) 
    elif message.text == "Поподробнеe":
        go_to_site_CSV(message)
    elif message.text == "Поподробнee":
        go_to_site_Time(message)
    elif message.text == "Поподрoбнee":
        go_to_site_Random(message)
    elif message.text == "Попoдрoбнee":
        go_to_site_Collections(message)
    elif message.text == 'Вложенные функции':
        bot.send_message(message.chat.id,"Вы выбрали тему-Функции:Вложенные функции",reply_markup=menu_vlog()) 
    elif message.text == 'Декораторы':
        bot.send_message(message.chat.id,"Вы выбрали тему-Функции:Декораторы",reply_markup=menu_Dekor())
    elif message.text == 'Замыкание':
        bot.send_message(message.chat.id,"Вы выбрали тему-Функции:Замыкание",reply_markup=menu_Zam())
    elif message.text == 'Рекурсивная функция':
        bot.send_message(message.chat.id,"Вы выбрали тему-Функции:Рекурсия",reply_markup=menu_rekur())   
    elif message.text == 'Определениe':
        bot.send_message(message.chat.id,"Вложенные (или внутренние, англ. inner, nested) функции – это функции, которые мы определяем внутри других функций. В Python такая функция имеет прямой доступ к переменным и именам, определенным во включающей её функции.") 
    elif message.text == 'Определeниe':
        bot.send_message(message.chat.id,"Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода.") 
    elif message.text == 'Опредeлeниe':
        bot.send_message(message.chat.id,"Замыкание — это функция, которая запоминает значения из своей внешней области видимости, даже если эта область уже недоступна. Она создается, когда функция объявляется, и продолжает запоминать значения переменных даже после того, как вызывающая функция завершит свою работу.") 
    elif message.text == 'Опрeдeлeниe':
        bot.send_message(message.chat.id,"Рекурсивная функция - это функция, содержащая в теле вызов самой себя. Помимо такого вызова, в теле функции обязательно должно быть терминальное условие, которое остановит повторные вызовы, чтобы они не стали бесконечными.") 
    elif message.text == "Подробное описаниe":
        go_to_site_vlog(message) 
    elif message.text == "Подробноe описаниe":
        go_to_site_dekor(message)
    elif message.text == "Подробное описание":
        go_to_site_zam(message)
    elif message.text == "Подробное oписание":
        go_to_site_rekur(message)
    elif message.text == 'Описание':
        bot.send_message(message.chat.id,"Вложенные (или внутренние, англ. inner, nested) функции – это функции, которые мы определяем внутри других функций. В Python такая функция имеет прямой доступ к переменным и именам, определенным во включающей её функции.") 
    elif message.text == 'Описаниe':
        bot.send_message(message.chat.id,"Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода.") 
    elif message.text == 'Описаниe':
        bot.send_message(message.chat.id,"Замыкание — это функция, которая запоминает значения из своей внешней области видимости, даже если эта область уже недоступна. Она создается, когда функция объявляется, и продолжает запоминать значения переменных даже после того, как вызывающая функция завершит свою работу.") 
    elif message.text == 'Oписaниe':
        bot.send_message(message.chat.id,"Рекурсивная функция - это функция, содержащая в теле вызов самой себя. Помимо такого вызова, в теле функции обязательно должно быть терминальное условие, которое остановит повторные вызовы, чтобы они не стали бесконечными.") 
    elif message.text == "Хочу подробнее":
        go_to_site_vlog(message) 
    elif message.text == "Хочу подробнеe":
        go_to_site_dekor(message)
    elif message.text == "Хочу подробнee":
        go_to_site_zam(message)
    elif message.text == "Хочу подрoбнee":
        go_to_site_rekur(message)
    elif message.text == 'Задачки':
        tasks_json(message)
    elif message.text == 'Назад к задачам json':
        tasks_json(message)
    elif message.text == 'Задача json 1':
        tasks_json_1(message)
    elif message.text == 'Решение задачи json 1':
        bot.send_message(message.chat.id, json_task_1_r)
    elif message.text == 'Задача json 2':
        tasks_json_2(message)
    elif message.text == 'Решение задачи json 2':
        bot.send_message(message.chat.id, json_task_2_r)
    elif message.text == 'Задача json 3':
        tasks_json_3(message)
    elif message.text == 'Решение задачи json 3':
        bot.send_message(message.chat.id, json_task_3_r)
    elif message.text == 'Задaчки CSV':
        tasks_csv(message)
    elif message.text == 'Назад к задачам csv':
        tasks_csv(message)
    elif message.text == 'Задача csv 1':
        tasks_csv_1(message)
    elif message.text == 'Решение задачи csv 1':
        bot.send_message(message.chat.id, csv_task_1_r)
    elif message.text == 'Задача csv 2':
        tasks_csv_2(message)
    elif message.text == 'Решение задачи csv 2':
        bot.send_message(message.chat.id, csv_task_2_r)
    elif message.text == 'Задача csv 3':
        tasks_csv_3(message)
    elif message.text == 'Решение задачи csv 3':
        bot.send_message(message.chat.id, csv_task_3_r)
    elif message.text == 'Зaдачки Random':
        tasks_random(message)
    elif message.text == 'Назад к задачам random':
        tasks_random(message)    
    elif message.text == 'Задача random 1':
        tasks_random_1(message)
    elif message.text == 'Решение задачи random 1':
        bot.send_message(message.chat.id, random_task_1_r)
    elif message.text == 'Задача random 2':
        tasks_random_2(message)
    elif message.text == 'Решение задачи random 2':
        bot.send_message(message.chat.id, random_task_2_r)
    elif message.text == 'Задача random 3':
        tasks_random_3(message)
    elif message.text == 'Решение задачи random 3':
        bot.send_message(message.chat.id, random_task_3_r)
    elif message.text == 'Зaдaчки Time':
        tasks_time(message)
    elif message.text == 'Назад к задачам time':
        tasks_time(message)
    elif message.text == 'Задача time 1':
        tasks_time_1(message)
    elif message.text == 'Решение задачи time 1':
        bot.send_message(message.chat.id, time_task_1_r)
    elif message.text == 'Задача time 2':
        tasks_time_2(message)
    elif message.text == 'Решение задачи time 2':
        bot.send_message(message.chat.id, time_task_2_r)
    elif message.text == 'Задача time 3':
        tasks_time_3(message)
    elif message.text == 'Решение задачи time 3':
        bot.send_message(message.chat.id, time_task_3_r)
    elif message.text == 'Задачи collection':
        tasks_collection(message)
    elif message.text == 'Назад к задачам collection':
        tasks_collection(message)
    elif message.text == 'Задача collection 1':
        tasks_collection_1(message)
    elif message.text == 'Решение задачи collection 1':
        bot.send_message(message.chat.id, collection_task_1_r)
    elif message.text == 'Задача collection 2':
        tasks_collection_2(message)
    elif message.text == 'Решение задачи collection 2':
        bot.send_message(message.chat.id, collection_task_2_r)
    elif message.text == 'Задача collection 3':
        tasks_collection_3(message)
    elif message.text == 'Решение задачи collection 3':
        bot.send_message(message.chat.id, collection_task_3_r)
    elif message.text == 'Задания':
        tasks_incfunck(message)
    elif message.text == 'Назад к задачам incfunck':
        tasks_incfunck(message)
    elif message.text == 'Задача incfunck 1':
        tasks_incfunck_1(message)
    elif message.text == 'Решение задачи incfunck 1':
        bot.send_message(message.chat.id, incfunck_task_1_r)
    elif message.text == 'Задача incfunck 2':
        tasks_incfunck_2(message)
    elif message.text == 'Решение задачи incfunck 2':
        bot.send_message(message.chat.id, incfunck_task_2_r)
    elif message.text == 'Задача incfunck 3':
        tasks_incfunck_3(message)
    elif message.text == 'Решение задачи incfunck 3':
        bot.send_message(message.chat.id, incfunck_task_3_r)
    elif message.text == 'Задaния':
        tasks_decor(message)
    elif message.text == 'Назад к задачам decor':
        tasks_decor(message)
    elif message.text == 'Задача decor 1':
        tasks_decor_1(message)
    elif message.text == 'Решение задачи decor 1':
        bot.send_message(message.chat.id, decor_task_1_r)
    elif message.text == 'Задача decor 2':
        tasks_decor_2(message)
    elif message.text == 'Решение задачи decor 2':
        bot.send_message(message.chat.id, decor_task_2_r)
    elif message.text == 'Задача decor 3':
        tasks_decor_3(message)
    elif message.text == 'Решение задачи decor 3':
        bot.send_message(message.chat.id, decor_task_3_r)
    elif message.text == 'Зaдaния':
        tasks_zam(message)
    elif message.text == 'Назад к задачам zam':
        tasks_zam(message)
    elif message.text == 'Задача zam 1':
        tasks_zam_1(message)
    elif message.text == 'Решение задачи zam 1':
        bot.send_message(message.chat.id, zam_task_1_r)
    elif message.text == 'Задача zam 2':
        tasks_zam_2(message)
    elif message.text == 'Решение задачи zam 2':
        bot.send_message(message.chat.id, zam_task_2_r)
    elif message.text == 'Задача zam 3':
        tasks_zam_3(message)
    elif message.text == 'Решение задачи zam 3':
        bot.send_message(message.chat.id, zam_task_3_r)
    elif message.text == 'Зaдания':
        tasks_recurs(message)
    elif message.text == 'Назад к задачам recurs':
        tasks_recurs(message)
    elif message.text == 'Задача recurs 1':
        tasks_recurs_1(message)
    elif message.text == 'Решение задачи recurs 1':
        bot.send_message(message.chat.id, recurs_task_1_r)
    elif message.text == 'Задача recurs 2':
        tasks_recurs_2(message)
    elif message.text == 'Решение задачи recurs 2':
        bot.send_message(message.chat.id, recurs_task_2_r)
    elif message.text == 'Задача recurs 3':
        tasks_recurs_3(message)
    elif message.text == 'Решение задачи recurs 3':
        bot.send_message(message.chat.id, recurs_task_3_r)
    elif message.text == 'FAQ':
        bot.send_message(message.chat.id, faq)
    elif message.text == 'Junior':
         send_june(message)
    elif message.text == 'Midle':
         send_middle(message)
    elif message.text == 'Senior':
         send_senior(message)
    elif message.text == 'About us':
        about_us(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)