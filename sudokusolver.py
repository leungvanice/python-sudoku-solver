board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9], 
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


# print_board(board)

def find_empty(board):
    emptyList = []
    for row in range(len(board)): 
        for i in range(len(board[row])): 
            if (board[row][i]) == 0: 
                pos = (row, i)
                emptyList.append(pos)
    return emptyList 

# print(find_empty(board))
