def greed():
    print(""" 
--------------------------------------
Приветсвуем вас в игре крестики-нолики  
--------------------------------------
формат ввода:   x y 
                x - номер строки  
                y - номер столбца  """)

def show_board(board):
    print(f"   (0) (1) (2)")
    for i in range(3):
        print(i, "|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("  -------------")

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def get_move():
    while True:
        cords = input('  Ваш ход: ').split( )

        if len(cords) != 2:
            print("Ошибка! Введите 2 координаты!")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print('Ошибка! Введите координвты цифрами!')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Ошибка - ваш ход вне поля! Уточните ввод!')
            continue

        if board[x][y] != " ":
            print("Клетка уже занята! Уточните ввод!")
            continue
        return x, y

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    elif board[2][0] == board[1][1] == board[0][2] != " ":
        return True
    return False

count = 0

greed()
current_player = 'X'
show_board(board)

print(f'Ходит игрок {current_player}')
for count in range(9):
    x, y = get_move()
    board[x][y] = current_player
    show_board(board)

    if check_win(board):
        show_board(board)
        print(f"ПОБЕДИЛ {current_player} !!!")
        break

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

