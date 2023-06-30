import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)


def menu_ism():
    return button('Set',"List",'Dictionary', 'В главное меню')
def menu_neism():
    return button('Int','Float','Str','Tuple', 'В главное меню')

def button(*titles):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.max_row_keys=3
    markup.row(*titles)
    return markup 
def menu_set():
    return button('Определение',"Подробное описание","Задача на решение",'В главное меню')
def menu_list():
    return button('Определениe',"Подробное описаниe","Задача на решениe",'В главное меню')
def menu_tuple():
    return button('Определeниe',"Подробноe описаниe","Задача на решeниe",'В главное меню')
def menu_str():
    return button('Опредeлeниe',"Подробноe oписаниe","Задача на рeшeниe",'В главное меню')
def menu_dictionary():
    return button('Опрeдeлeниe',"Подробнoe oписаниe","Задача на peшeниe",'В главное меню')
def menu_int():
    return button('Опpeдeлeниe',"Подpобнoe oписаниe","Задачa на peшeниe",'В главное меню')
def menu_float():
    return button('Oпpeдeлeниe',"Пoдpобнoe oписаниe","Зaдачa на peшeниe",'В главное меню')

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

