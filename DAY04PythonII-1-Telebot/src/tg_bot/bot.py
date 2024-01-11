import telebot
import random
import datetime as dt
from telebot import types

file = open('token.txt', 'r')
token = file.readline()

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, "Готов")
def start_handler(message):
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться в ответ") 
    btn2 = types.KeyboardButton("Что ты умеешь?")
    reply_markup.add(btn1, btn2) 
    input = bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}", reply_markup = reply_markup) # Как обычно выводим сообщение, но указываем, что пользователь увидит reply-клавиатуру.
    bot.register_next_step_handler(input, reply)
    
def reply(message):
    if message.text == 'Привет Robobot!':
        bot.send_message(message.chat.id, "Спасибо, ты очень любезен")
    elif message.text == 'Что ты умеешь?':
        bot.send_message(message.chat.id, "Много чего")
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/help") 
        btn2 = types.KeyboardButton("/minigame")
        btn3 = types.KeyboardButton("/age")
        btn4 = types.KeyboardButton("/name")
        btn5 = types.KeyboardButton("/predict")
        btn6 = types.KeyboardButton("Вернуться в предыдущее меню")
        key.add(btn1, btn2, btn3, btn4, btn5, btn6)
        input = bot.send_message(message.chat.id, "Выберете кнопку из меню справа", reply_markup=key)
        bot.register_next_step_handler(input, handle_menu)
        
def handle_menu(message):
    if message.text == '/help':
        process_help(message)
    elif message.text == '/minigame':
        process_game(message)
    elif message.text == '/age':
        process_age(message)
    elif message.text == '/name':
        process_name(message)
    elif message.text == '/predict':
        process_predict(message)
    elif message.text == 'Вернуться в предыдущее меню':
        start_handler(message)
        
        
#echo-bot
     
# @bot.message_handler(content_types=['text'])
# def echo(message):
#     bot.send_message(message.chat.id, message.text)    


users = {}
age = -1
name= None

upper_limit = 101
lower_limit = 1
guess = 50
counter = 0


@bot.message_handler(commands=['age'])
def process_age(message):
    input = bot.send_message(message.chat.id, "Введите возраст")
    bot.register_next_step_handler(input, ages)
    
def ages(message):
    if (message.text).isdigit():
        bot.send_message(message.chat.id, message.text)
        global users, age, name
        age= int(message.text)
        if message.from_user.id in users.keys():
            users[message.from_user.id] =  {list(users[message.from_user.id].keys())[0]: age}
        else:
            users[message.from_user.id] =  {name: age}
        print(users)


@bot.message_handler(commands=['name'])
def process_name(message):
    input = bot.send_message(message.chat.id, "Введите имя")
    bot.register_next_step_handler(input, names)
    
def names(message):
    bot.send_message(message.chat.id, message.text)
    global users, age, name
    name= message.text
    if message.from_user.id in users.keys():
        users[message.from_user.id] =  {name: (list(users[message.from_user.id].values())[0])}
    else:
        users[message.from_user.id] =  {name: age}
    print(users)

@bot.message_handler(commands=['help'])
def process_help(message):
    bot.send_message(message.chat.id, "/age - пользователь должен свой возраст \n/\
name - пользователь должен ввести свое имя \n/help - вывод информации о доступных командах бота\n\
/predict - выводит предсказание о твоем возрасте в случайный год\n\
/minigame - миниигра, в которой бот отгдает загаданное тобой число")

@bot.message_handler(commands=['predict'])
def process_predict(message):
    if message.from_user.id in users.keys():
        
        date = int(dt.datetime.now().year)
        random_year = int(random.uniform(date, date+100))
        if list(users[message.from_user.id].keys())[0]:
            user_age = list(users[message.from_user.id].values())[0]
            user_name = list(users[message.from_user.id].keys())[0]
            if user_age != -1:
                bot.send_message(message.chat.id, f"Я вижу, вижу, что Вам, {user_name}, в {random_year} году будет {user_age + random_year- date}")
            else:
                bot.send_message(message.chat.id, "Вы не ввели возраст. Введите его с помощью команд /age")
        else:
            bot.send_message(message.chat.id, "Вы не ввели имя. Введите его с помощью команд /name")
    else:
        bot.send_message(message.chat.id, "Вы не зарегестрировались. Зарегестрируйтесь с помощью команд /age и /name")

@bot.message_handler(commands=['minigame'])
def process_game(message):
    bot.send_message(message.chat.id, "Загадайте число от 1 до 100. Я постараюсь отгадать это число. Вам предстоит поправлять меня, используя клавиши 'Больше' или 'Меньше' Если я угадал, нажмите клавишу 'Ответ' Начнем.")
    markup = types.InlineKeyboardMarkup()
    btn_url = types.InlineKeyboardButton(text='Больше', callback_data = "more") 
    btn_switch = types.InlineKeyboardButton(text='Меньше', callback_data = "less") 
    btn_callback = types.InlineKeyboardButton(text='Ответ', callback_data = "answer") 
    markup.add(btn_url, btn_switch, btn_callback) 
    bot.send_message(message.chat.id, "50", reply_markup = markup)
    
@bot.callback_query_handler(func=lambda call: True)
def process_guess(call):
    global upper_limit, lower_limit, guess, counter
    if call.data == 'more':
        lower_limit = guess
        print(f"in more: lower limit is {lower_limit} and upper_limit is {upper_limit}")
    elif call.data == 'less':
        upper_limit = guess
        print(f"in less: lower limit is {lower_limit} and upper_limit is {upper_limit}")
    else:
        bot.send_message(call.message.chat.id, f'Я молодец!!! Отгадал за {counter} попыток.')
        counter = 0
        upper_limit = 101
        lower_limit = 1
        guess = 50
        return counter
    counter +=1
    guess = int(random.uniform(lower_limit, upper_limit))
    bot.send_message(call.message.chat.id, guess)
bot.infinity_polling()


# Ты можешь вынести функцию пересмешника в отдельный блок (например, /mockingbird) либо оставить в основном блоке обработки сообщений
# НО не удаляй эту функциональность (а вот token.txt удали перед отправкой на удалённый репозиторий)
# Функциональность предсказателя также не убирай!

# Да прибудет с тобой сила, Python-разработчик!
# ЗАДАНИЕ #1
# Заведи телеграмм бота (обратись, но с УВАЖЕНИЕМ, к @BotFather). Он, возможно, выдаст тебе токен
# Никому не передавай свой токен. Добавь его в файл token.txt. НЕ ЗАБУДЬ УДАЛИТЬ ФАЙЛ ПЕРЕД ОТПРАВКОЙ ЗАДАНИЯ В УДАЛЁННЫЙ РЕПОЗИТОРИЙ!
# Сделай так чтобы бот обрабатывал базовую команду /start и что-то отвечал "Готов!" или иное. Это будет "активацией" бота
# Напиши бота-пересмешника, который возвращает тот текст, который ввёл пользователь
# Например, Пользователь ввёл "Привет", бот ответил "Привет". Пользователь спросил "Как дела?", бот в ответ "Как дела?"


# ЗАДАНИЕ #2
# После того как бот-пересмешник готов. Давай добавим новый функционал. Необходимо завести функции, которые обрабатывают команды:
# a) /age
# б) /name
# в) /help
# Первая предлагает пользователю ввести возраст (подумай как считать ответ и к какому типу его привести),
# вторая предлагает пользователю ввести имя (подумай как считать ответ)
# третья выводит информацию о всех командах, которые поддерживает бот
# Данные о пользователе будем запоминать в глобальную переменную users - словарь, где ключ - это ID пользователя, 
# а значение - словарь из двух элементов: age, name; которые соответствуют значениям, введённым пользователем
# Давай используем эти данные для новой функции
# будем обрабатывать команду /predict, которая будет выводить следующий текст:
# "Я вижу, вижу, что Вам, {name}, в {year} будет {age}!"
# где name - это имя пользователя,
# year - рандомный год (целое число!) в диапазоне от [текущий год; текущий год + 100]
# age - возраст пользователя в year году
# То есть для пользователя Имярек, которому в 2000 году 20 лет бот может выдать следующий результат:
# "Я вижу, вижу, что Вам, Имярек, в 2020 будет 40!"
# Обработать случай если /age, /name пустые! 


# Задание #3
# Давай перенесём команду /help в отдельное меню (Menu), как у @BotFather
# Посмотри в Интернете как создать такое меню (Подсказка: для решения задачи необходимо обратиться С УВАЖЕНИЕМ к Отцу всех ботов =])
# После создания меню перейдём к созданию нового интерактива с ботом - кнопки! (возможно тебе понадобится дополнительный модуль - используй конструкцию import ... или from ... import ...)
# Добавь новую команду (/minigame), чтобы поиграть с пользователем в угадайку: пользователь загадывает число от 1 до 100, а бот пытается отгадать
# Пусть каждый ответ бота имеет три inline кнопки: Больше, Меньше, Ответ
# И игра продолжается пока пользователь не нажмёт кнопку "Ответ" (подумай как бот должен отгадывать число, рандом тут может сыграть злую шутку!)


# Задание #4 
# Добавим дополнительные кнопки в интерфейс нашего бота (reply кнопки)
# Пусть при вводе команды /start бот здоровается с пользователем по никнейму в TG (first & last name пользователя)
# У бота должны отображаться (под строкой ввода текста) несколько кнопок:
# 1) Поздороваться в ответ (при нажатии бот отвечает пользователю, что у того хорошие манеры)
# 2) Что ты умеешь? (Выводит информацию о доступных командах и переводит в подменю, где команды заданы в виде кнопок)
# При нажатии на кнопку 2 меню меняется на иное:
# 1) набор кнопок, соответствующих командам /help, /minigame и др.
# 2) кнопка возврата в начальное меню
