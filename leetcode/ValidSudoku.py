'''
https://leetcode.com/problems/valid-sudoku/
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check violations in rows

        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[i][j] != '.' and board[i][j] in seen:
                    print("Row Conflict: ", i, j)
                    return False
                else:
                    seen.add(board[i][j])
        
        # Check violations in cols

        for j in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                if board[i][j] != '.' and board[i][j] in seen:
                    print("Col Conflict: ", i, j)
                    return False
                else:
                    seen.add(board[i][j])

        # Check violations in 3x3

        for currSubGridRow in range(0, len(board), 3):
            for currSubGridCol in range(0, len(board[0]), 3):
                seen = set()
                for i in range(0,3):
                    for j in range(0,3):
                        toCheckR = currSubGridRow + i
                        toCheckC = currSubGridCol + j
                        if board[toCheckR][toCheckC] != '.' and board[toCheckR][toCheckC] in seen:

                            print("Subgrid: ", toCheckR, toCheckC)
                            return False
                        else:
                            seen.add(board[toCheckR][toCheckC])
        
        return True


