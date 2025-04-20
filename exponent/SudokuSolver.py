'''
Input: 2D matrix
Out: boolean

https://www.tryexponent.com/practice/prepare/sudoku-solver
'''


from typing import List

def getOptions(board: List[List[str]], row: int, col: int):
    notValid = set()
    # Check row constraints
    for j in range(0,len(board[0])):
        notValid.add(board[row][j])

    # Check column constraints
    for i in range(0,len(board)):
        notValid.add(board[i][col])

    # Check 3x3 subgrid constraints
    subgridRow = row // 3
    subgridCol = col // 3
    for i in range(0,3):
        for j in range(0,3):
            notValid.add(board[subgridRow*3 + i][subgridCol*3 + j])

    options = []
    # Make options list
    for i in range(1,10):
        if str(i) not in notValid:
            options.append(str(i))
    
    return options

def solveHelper(board: List[List[str]], row: int, col: int):
    # Base Case
    if row >= len(board):
        return True
    
    if board[row][col] != '.':
        nextRow = row + (col + 1) // 9
        nextCol = (col + 1) % 9
        return solveHelper(board, nextRow, nextCol)

    options = getOptions(board, row, col)

    if len(options) == 0:
        return False

    hasValidSol = False
    for val in options:
        oldVal = board[row][col]
        board[row][col] = val

        nextRow = row + (col + 1) // 9
        nextCol = (col + 1) % 9

        # if col == len(board[0]) - 1:
        #     nextRow = row + 1
        #     nextCol = 0
        # else:
        #     nextCol = col + 1

        hasValidSol = hasValidSol or solveHelper(board, nextRow, nextCol)
        board[row][col] = oldVal

    
    return hasValidSol

def sudoku_solve(board: List[List[str]]) -> bool:
    
    return solveHelper(board, 0, 0)

    # Return a boolean representing if solvable 

  
# debug your code below
board = [
    [".", ".", ".", "7", ".", ".", "3", ".", "1"],
    ["3", ".", ".", "9", ".", ".", ".", ".", "."],
    [".", "4", ".", "3", "1", ".", "2", ".", "."],
    [".", "6", ".", "4", ".", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "1", ".", ".", "8", ".", "4", "."],
    [".", ".", "6", ".", "2", "1", ".", "5", "."],
    [".", ".", ".", ".", ".", "9", ".", ".", "8"],
    ["8", ".", "5", ".", ".", "4", ".", ".", "."]
]

print(sudoku_solve(board))
