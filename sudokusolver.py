board = [
    [0, 7, 0, 0, 0, 0, 0, 0, 9],
    [5, 1, 0, 4, 2, 0, 6, 0, 0],
    [0, 8, 0, 3, 0, 0, 7, 0, 0],
    [0, 0, 8, 0, 0, 1, 3, 7, 0],
    [0, 2, 3, 0, 8, 0, 0, 4, 0],
    [4, 0, 0, 9, 0, 0, 1, 0, 0],
    [9, 6, 2, 8, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 1, 0, 4, 0, 0],
    [7, 0, 0, 2, 0, 3, 0, 9, 6],
]


def print_board(board):
    for row in range(len(board)):
        rowString = ""
        for i in range(len(board[row])):
            rowString += str(board[row][i]) + ' '
            if (i + 1) % 3 == 0 and i != 0 and i != 8:
                rowString += '| '
        print(rowString)
        if (row+1) % 3 == 0 and row != 0 and row != 8:
            print('------ ------- ------')


print_board(board)
