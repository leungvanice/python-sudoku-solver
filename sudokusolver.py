# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9],
# ]

board = [
    [3, 0, 0, 8, 0, 1, 0, 0, 2],
    [2, 0, 1, 0, 3, 0, 6, 0, 4],
    [0, 0, 0, 2, 0, 4, 0, 0, 0],
    [8, 0, 9, 0, 0, 0, 1, 0, 6],
    [0, 6, 0, 0, 0, 0, 0, 5, 0],
    [7, 0, 2, 0, 0, 0, 4, 0, 9],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [9, 0, 4, 0, 8, 0, 7, 0, 5],
    [6, 0, 0, 1, 0, 7, 0, 0, 3],
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


def check_valid(board, pos, insertNum):
    def getColList(board, colNum):
        col = []
        for r in board:
            col.append(r[colNum])
        return col

    def getGridList(board, rowNum, colNum):
        gridList = []
        grouping = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        xGrp = []
        yGrp = []
        for grp in grouping:
            if rowNumber in grp:
                xGrp = grp
            if colNumber in grp:
                yGrp = grp
        for i in range(len(xGrp)):
            for j in range(len(yGrp)):
                pos = (i, yGrp[j])
                gridList.append(pos)
        return gridList
    rowNumber = pos[0]
    colNumber = pos[1]
    # Get numbers in row, column, grid
    row = board[rowNumber]
    col = getColList(board, colNumber)
    grid = getGridList(board, rowNumber, colNumber)

    # Check valid
    if insertNum in row or insertNum in col or insertNum in grid:
        return False
    else:
        return True


# result = check_valid(board, (0, 1), 8)
# print(result)
