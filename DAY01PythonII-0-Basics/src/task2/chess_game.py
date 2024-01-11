# Допиши код
# Функция reach_pos должна возращать значение True,
# если фигура может достичь pos1 из pos0 за ОДИН шаг, и False в обратном случае

def reach_pos(pos0, pos1, piece):
    if piece == 'king':
        if abs(pos0[0] - pos1[0]) <= 1 and abs(pos0[1] - pos1[1]) <= 1:
            return True
    elif piece == 'rook':
        if pos0[0] == pos1[1] or pos0[1] == pos1[1]:
            return True
    elif piece == 'bishop':
        if abs(pos0[0] - pos1[0]) == abs(pos0[1]- pos1[1]):
            return True
    elif piece == 'knight':
        if (abs(pos0[0] - pos1[0]) == 1 and abs(pos0[1]- pos1[1]) == 2) or (abs(pos0[0] - pos1[0]) == 2 and abs(pos0[1]- pos1[1]) == 1):
            return True
    return False


while True:
    try:
        # Считай ввод пользователя:
        # start = input()
        # finish = input()
        figures = ['knight', 'rook', 'bishop', 'king']
        # figure = input()
        # 1) Первая строка - это начальная позиция фигуры (два числа через пробел)
        # 2) Вторая строка - это конечная позиция фигуры (два числа через пробел)
        # 3) Третья строка - это фигура (knigt, rook, bishop, or king)
    
        # Раздели строки на два целых числа
        # Помни, числа могут быть в диапазоне от 1 до 8
        x0, y0 = (map(int, input().split()))
        x1, y1 = (map(int, input().split()))
        # Считай наименование шахмтной фигуры
        # Помни, наименование фигуры может содержать и прописные, и строчные буквы
        # Возможно "лишние" пробельные символы
        piece = input().lower().replace(' ', '')
        try:
            1<=x0<=8 and 1<=x1<=8 and 1<=y0<=8 and 1<=y1<=8 and piece in figures
            # print("ddf")
        except:
            print("Некорректный ввод") # Не убирай print! Он нужен для проверки твоего решения =)
        
        print(reach_pos([x0, y0], [x1, y1], piece))
    except EOFError:
        break


# Даны две различные клетки шахматной доски (ввод клетки – два числа от 1 до 8 – номера строки и столбца),
#  также вводится название фигуры, которая стоит на первой клетке (knigt, rook, bishop or king). Кроме этой
#   фигуры на доске никого нет. Определи, может ли данная фигура попасть на 2ю клетку за один ход.

# Для проверки своего решения воспользуйся файлами в директории materials/task2/.

# Способ запуска проверки:

# python src/task2/chess_game.py < materials/task2/cases.txt | python materials/task2/checker.py

# Файл с самим заданием – materials/task2/chess_game.py.

# Результат сохрани в файле chess_game.py в папке src.