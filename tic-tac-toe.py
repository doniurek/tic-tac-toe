def print_board(board):
    final_string = ''
    for line in range(len(board)):
        for field in range(len(board[line])):
            final_string = final_string + ' | ' + str(board[line][field])
        final_string = final_string + ' | \n -------------\n'
    final_string = ' -------------\n' + final_string
    print(final_string)

def set_symbol(board, symbol, position):
    # board[(position-1)//3][(position-1)%3] = symbol
    if position < 4:
        board[0][position-1] = symbol
    elif position < 7:
        board[1][position-4] = symbol
    else:
        board[2][position-7] = symbol

def check_move(board, position):
    if not position in range(1,10):
        return False
    # symbol = board[(position-1)//3][(position-1)%3]
    if position < 4:
        symbol = board[0][position-1]
    elif position < 7:
        symbol = board[1][position-4]
    else:
        symbol = board[2][position-7]
    return type(symbol) == int

def won(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] or \
            board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return True
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] or \
        board[0][2] == board[1][1] and board[0][0] == board[2][0]:
        return True
    return False

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print_board(board)

for i in range(1,10):
    if i % 2 != 0:
        symbol = 'O'
        print("Gdzie chcesz postawić kółko?")
    else:
        symbol = 'X'
        print("Gdzie chcesz postawić krzyżyk?")

    try:
        position = int(input("Podaj numer pola: "))
    except ValueError:
        position = 0

    while not check_move(board, position):
        try:
            position = int(input("Niepoprawny numer pola, spróbuj jeszcze raz: "))
        except ValueError:
            position = 0

    set_symbol(board, symbol, position)

    print_board(board)

    if i > 4 and won(board):
        print("Wygrywa", symbol+". Gratulacje!")
        exit()

print("Remis!")
