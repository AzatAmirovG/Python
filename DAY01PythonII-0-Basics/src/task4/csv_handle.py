import csv
import time
import random
import datetime as dt


# Допиши код
# Необходимо составить файл csv со следующими колонками:
# 1) номер записи
# 2) текущая дата
# 3) timestamp
# 4) температура
# 5) курс валюты


def current_date():
    # Допиши код
    # Нужно получить дату следующего вида
    # год-месяц-день часы:минуты:секунда (пример, 2023-08-30 11:01:36)
    now = dt.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def timestamp():
    # Допиши код
    # Нужно получить UNIX-time в миллисекундах
    # возможно тебе понадобиться округление
    return int(round(time.time() * 1000))

def current_temperature():
    # Допиши код
    # Давай представим, что мы работники Гидрометцентра (какой-нибудь выдуманной страны)
    # Будет определять текущую температуру с помощью рандома!
    # Выбери в модуле random равномерное распределение (uniform) со значениями от -50 до 50
    # Температура должна быть записана с ОДНИМ знаком после запятой
    return round(random.uniform(-50,50), 1)

def current_exchange_rate():
    # Допиши код
    # Давай представим, что мы работники Центробанка (какой-нибудь выдуманной страны)
    # Будет определять текущий курс нашей валюты к валюте соседней страны с помощью рандома!
    # Выбери в модуле random гамма распределение (gammavariate) со значениями от alpha=4, beta=2
    # Курс валюты должен быть записана с ДВУМЯ знаками после запятой
    return round(random.gammavariate(4, 2), 2)
    pass


# Количество записей N
# После каждоо замера сделай задержку на 0.1 секунду
# N = 300
# for i in range(N):
#     pass

# Запиши результаты в файл results.csv
with open('../../src/task4/results.csv', 'w', newline='') as file:
    file_writer = csv.writer(file, delimiter = "\t")
    N = 300
    for i in range(N):
        file_writer.writerow([i, current_date(), timestamp(), current_temperature(), current_exchange_rate()])
        time.sleep(0.1)
