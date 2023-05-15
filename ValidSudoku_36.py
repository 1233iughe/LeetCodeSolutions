'''

'''
#Set based by julialokot
class Solution(object):
    def isValidSudoku(self, board):
        #Here she stores a list per element
        res = []
        #Looping through the board
        for i in range(9): #Rows
            for j in range(9):#Cols
                #Accessing the element
                element = board[i][j]
                #Validating the input (must be a number)
                if element != '.':
                    '''
                    Creates a list of tuples containing 3 pieces of information
                    1. (row, element)
                    2. (col, element)
                    3. (sub-grid row, sub-grid col, element)
                    Sub grids are (0,0) - (2,2)
                    '''
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        #Each list of tuples should be unique in a correct board
        return len(res) == len(set(res))

#Brute force set-based
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Validating rows and columns
        rows = [set() for i in range(9)]
        col = set()

        for i in range(9):
            col.clear()
            #print(col)
            for j in range(9):
                cell = board[j][i]
                if cell in col or cell in rows[j]:
                    return False
                if cell != '.':
                    col.add(cell)
                    rows[j].add(cell)
           # print(rows)
        sub = set()
        for i in range(2,9,3):
            for j in range( 2, 9,3):
                sub.clear()
                #print(i,j)
                x =''.join([
                    board[i-2][j-2], board[i-2][j-1], board[i-2][j],
                    board[i-1][j-2], board[i-1][j-1], board[i-1][j],
                    board[i][j-2], board[i][j-1], board[i][j]
                ])
                #print(x)
                for char in x:
                    if char != '.' and char in sub:
                        return False
                    sub.add(char)

        return True