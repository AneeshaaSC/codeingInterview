class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        if (len(board) != 9 or len(board[0]) != 9):
            return False
            
        for x in range(len(board)):
            tempDict = {}
            for y in range(len(board[0])):
                if (board[x][y] == '.'):
                    continue
                if (tempDict.has_key(board[x][y])):
                    return False
                else:
                    tempDict.update({board[x][y]:0})
            
        for y in range(len(board[0])):
            tempDict = {}
            for x in range(len(board)):
                if (board[x][y] == '.'):
                    continue
                if (tempDict.has_key(board[x][y])):
                    return False
                else:
                    tempDict.update({board[x][y]:0})    

        for bigX in range(3):
            for bigY in range(3):
                tempDict = {}
                for x in range(bigX * 3, bigX * 3 + 3):
                    for y in range(bigY * 3, bigY * 3 + 3):
                        if (board[x][y] == '.'):
                            continue
                        if (tempDict.has_key(board[x][y])):
                            return False
                        else:
                            tempDict.update({board[x][y]:0})   


        return True
        
        
