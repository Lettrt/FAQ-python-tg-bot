import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)


def menu():
    return button('Изменяемые','Неизменяемые')
def menu_ism():
    return button('Int','Float','Str','Tuple')
def menu_neism():
    return button('Set',"List",'Dictionary')

def button(*titles):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.max_row_keys=3
    markup.row(*titles)
    return markup 
def menu_set():
    return button('Определение',"Подробное описание","Задача на решение",'Возврат к главному меню')
def menu_list():
    return button('Определениe',"Подробное описаниe","Задача на решениe",'Возврат к главному меню')
def menu_tuple():
    return button('Определeниe',"Подробноe описаниe","Задача на решeниe",'Возврат к главному меню')
def menu_str():
    return button('Опредeлeниe',"Подробноe oписаниe","Задача на рeшeниe",'Возврат к главному меню')
def menu_dictionary():
    return button('Опрeдeлeниe',"Подробнoe oписаниe","Задача на peшeниe",'Возврат к главному меню')
def menu_int():
    return button('Опpeдeлeниe',"Подpобнoe oписаниe","Задачa на peшeниe",'Возврат к главному меню')
def menu_float():
    return button('Oпpeдeлeниe',"Пoдpобнoe oписаниe","Зaдачa на peшeниe",'Возврат к главному меню')


@bot.message_handler(content_types=["text"])
def main_func(message):
    if message.chat.type=="private":
        if message.text == 'Определение':
            bot.send_message(message.chat.id,'Set, оно же множество-структура, содержащая неповторяющиеся элементы в случайном порядке')
        elif message.text == 'Set':
            bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Set-множество",reply_markup=menu_set()) 
        elif message.text == 'List':
            bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: List-списки",reply_markup=menu_list())
        elif message.text == 'Tuple':
            bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Tuple-кортежи",reply_markup=menu_tuple())
        elif message.text == 'Str':
            bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Str-строки",reply_markup=menu_str())   
        elif message.text == 'Определениe':
            bot.send_message(message.chat.id,"Это удобный способ хранения данных с возможностью их изменения") 
        elif message.text == 'Dictionary':
            bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Dictionary-словари",reply_markup=menu_dictionary())   
        elif message.text == 'Int':
            bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Integer",reply_markup=menu_int())  
        elif message.text == 'Float':
            bot.send_message(message.chat.id,"Вы выбрали тему-типы данных: Float",reply_markup=menu_float())
        elif message.text == 'Определениe':
            bot.send_message(message.chat.id,"Это удобный способ хранения данных с возможностью их изменения") 
        elif message.text == 'Определeниe':
            bot.send_message(message.chat.id,"Способ хранить различные типы данных в одной переменной,но без возможности её изменения") 
        elif message.text == 'Опредeлeниe':
            bot.send_message(message.chat.id,"Это любые данные взятые в ковычки") 
        elif message.text == 'Опрeдeлeниe':
            bot.send_message(message.chat.id,"Неупорядоченные коллекции произвольных данных в формате ключ-значение") 
        elif message.text == 'Опpeдeлeниe':
            bot.send_message(message.chat.id,"Все целые числа имеют тип Integer") 
        elif message.text == 'Oпpeдeлeниe':
            bot.send_message(message.chat.id,"Все числа с плавающей точкой имеют тип Float") 
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

def go_to_site_set(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://python-scripts.com/sets")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по типу данных set', reply_markup=keyboard)

def go_to_site_list(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://metanit.com/python/tutorial/3.1.php")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по типу данных list', reply_markup=keyboard)

def go_to_site_tuple(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://younglinux.info/python/tuple")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по типу данных tuple', reply_markup=keyboard)

def go_to_site_str(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по типу данных str', reply_markup=keyboard)

def go_to_site_dictionary(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по типу данных dictionary', reply_markup=keyboard)

def go_to_site_int(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://informatics.msk.ru/mod/book/view.php?id=42177#:~:text=%D0%94%D0%BB%D1%8F%20%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20%D1%86%D0%B5%D0%BB%D1%8B%D1%85%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%B2,%D0%BE%D0%B1%D1%8B%D1%87%D0%BD%D0%BE%20%D0%B7%D0%B0%D0%BD%D0%B8%D0%BC%D0%B0%D0%B5%D1%82%20%D0%BB%D0%B8%D1%88%D1%8C%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%B1%D0%B0%D0%B9%D1%82).")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по типу данных int', reply_markup=keyboard)

def go_to_site_float(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробное описание",url="https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-float-veschestvennye-chisla/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Справочник по типу данных float', reply_markup=keyboard)

