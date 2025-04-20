from collections import deque 
'''

https://leetcode.com/problems/01-matrix/description/

Strategies:

- Clarifying questions about the current question 
    - edge cases
    - confirming input output
- Make more test cases, solve them by hand
    - edge cases, remove symmetry, core cases


'''

'''
Input: mat = [[0,0,0],
              [0,1,1],
              [1,1,1]]

mat = [[A,B,C],
        [D,E,F],
        [G,1,1]]

Output: [ [0,-1,-1], 
          [-1,-1,-1],
          [-1,-1,-1] ]

Queue: t - [(1,0), (0,2), (0,1), (0,0)] - h

        t                h

currIndex = (0,2) 

Output: [ [0,0,0], 
          [0,1,1],
          [1,2,2]]

Edge Cases: 
- Board can be size 1
- At least one 0
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        out = [[-1 for _ in range(0,len(mat[0]))] for _ in range(0,len(mat))]
        neighbors = [(0,1), (1,0), (0,-1), (-1,0)]

        myQ = deque()
        # If zero, then dist is zero
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                if mat[i][j] == 0:
                    myQ.append((i, j))
                    out[i][j] = 0


        while myQ:
            x, y = myQ.popleft()

            visited = (x,y)

            # print(x,y)
            # print(myQ)
            if mat[x][y] == 0:
                out[x][y] = 0

            minDist = float(inf)

            # Check all neighboring nodes
            for dX, dY in neighbors:
                # Make sure valid index
                if x + dX < 0 or x + dX >= len(mat) or y + dY < 0 or y + dY >= len(mat[0]):
                    continue

                # Check if visited, if so then update min dist
                if out[x+dX][y+dY] != -1:
                    minDist = min(minDist, out[x+dX][y+dY] + 1)
                else: # otherwise append to queue
                    myQ.append((x+dX, y+dY))
            
            if mat[x][y] != 0:
                out[x][y] = minDist
                     


        # return: matrix of same size, newMat[i] = distance of nearest 0 for each cell i in mat
        return out
