# Используй модуль datetime для работы с датами и календарём
import datetime as dt

# Если возникла ошибка ModuleNotFoundError: No module named '<module_name>'
# Попробуй установить модуль с помощью команды pip install <module_name> 


# Допиши код
def how_unlucky(y):
    counter = 0
    for i in range(1,13):
        date = dt.date(year,i,13)
        if date.weekday() == 4:
            counter+=1
    return counter

# Считай год, который ввёл пользователь
# Попробуй ввести следующие года: -1, 0, 9999, 10000
# Подумай над проверками корректности ввода (тут может помочь оператор if)
try:
    year = int(input())
    int(year)
    print(how_unlucky(year))
except ValueError:
    print("Вы ввели некорректный год")



# else:
#     print("Вы ввели не число")


# Написать функцию, которая по номеру года определит, сколько в этом году было/будет пятниц,
# выпадающих на 13е число. Файл с заданием находится в директории materials/task1/friday-the-13th.py.
# Результат сохрани в файле friday.the_13th.py в папке src.