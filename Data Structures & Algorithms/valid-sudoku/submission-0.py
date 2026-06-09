import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        b = np.array(board)
        T = b.T
        S = self.makesquares(b)

        if self.checkrow(b) and self.checkrow(T) and self.checkrow(S):
            return True

        return False

             

    

    def checkrow(self, board):
        
        for row in board:
            c = {}
            for i in row:
                if i == ".":
                    continue
                if i in c:
                    return False
                else:
                    c[i] = 1

        return True

    def makesquares(self, board):

        blocks = []
        
        for i in range(3):
            for j in range(3):
        
                blocks.append(board[i*3:i*3+3, j*3:j*3+3].flatten())


        return blocks

    

