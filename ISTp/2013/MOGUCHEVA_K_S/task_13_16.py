#Задача 13. Вариант 16.
#Разработайте  игру "Крестики-нолики". (см. М.Доусон Программируем на Pyton гл.6)
#Разработайте собственную стратегию ходов компьютера для игры "Крестики-нолики".
#Перепишите функцию computer_move() в сооответствии с этой стратегией.

#Mogucheva K.S.
#27.11.2016


# Компьютер играет в игру крестики-нолики против пользователя.
#глобальные константы
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruct():
    """Выводит на экран инструкцию для игрока."""
    print(
    """
    Добро пожаловать в игру "Крестики-нолики".
    Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соотвествуют полям
    доски - так, как показано ниже:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

    
	Приготовься к бою!!! Вот-вот начнется решающее  сражение.
    """
    )


def ask_yes_no(question):
    """Задает вопрос с ответом 'да' или 'нет'"""
    response = None
    while response not in ("да", "нет"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Просит вести число из диапозона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определяет принадлежность перового хода."""
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (да, нет): ")
    if go_first == "да":
        print("\nНу, что ж, даю тебе фору!Играй крестиками.")
        human = X
        computer = O
    else:
        print("\nТвоя удаль тебя погубит!Буду начинать я.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Создаёт новую игровую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает игровую доску на экране."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8])


def legal_moves(board):
    """Создаёт список доступных ходов."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя в игре."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    """Получает ход человек"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭто поле уже занято. Выбери другое.\n")
    print("Ладно...")
    return move


def computer_move(board, computer, human):
    """Делает ход за компьютерного противника."""
    # создадим рабочую копию доски, потому что функция будет менять некотороые элементы в списке
    board = board[:]
    # ходы, от лучшего к худшему
    BEST_MOVES = (4, 8, 5, 3, 7, 6, 1, 0, 2)

    print("Я выберу поле номер", end = " ")
    # если сдедующим ходом может победить компьютер, выберем этот ход
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # выполнив проверку этого хода, отменим его (в локальной копии игровой доски)
        board[move] = EMPTY

    # если следующим ходом может победить чегловек, блокируем этот ход
    for moves in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # выполнив проверку этого хода, отменим его (в локальной копии игровой доски)
        board[move] = EMPTY

    # поскольку следующим ходом ни одна из сторон не может победить,
    # выберем лучшее из доступных полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Осуществляет переход хода."""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры."""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Как я и предсказал победа осталась за мной!\n")
    elif the_winner == human:
        print("поздравляю! ты сумел прехитрить меня!\n")
    elif the_winner == TIE:
        print("игра вничью. \n")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# запуск программы
main()
input("Нажмите Enter, чтобы выйти.")
