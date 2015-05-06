import copy
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        result = []
        table = [['.' for i in range(n)] for i in range(n)]
        dictColumn = {}
        self.helper(table, result,  n, dictColumn,0,0)   
        for i in range(len(result)):
            for y in range(len(table)):
                result[i][y] = ''.join(result[i][y])
        return result
        
    def helper(self, table, result, n, dictColumn, currentX,currentY):
        if (n == 0):
#            print table
            result.append(copy.deepcopy(table))
        else:
            x = currentX
            for  y in range(len(table)):
#                print table
#                print "x",x,"y",y
#                print "column",dictColumn
                if (dictColumn.get(y) == None and self.diagonal(x,y,table)) :
#                    orTable = copy.deepcopy(table) 
                    orColumn = dictColumn.copy()
                    table[x][y] = 'Q'   
                    dictColumn.update({y:1})
                    self.helper(table,result,n-1, dictColumn ,x+1,y)
                    table[x][y] = '.'   
                    dictColumn = orColumn
                    
                    
  
    def diagonal(self,x,y,table):
        tempX = x
        tempY = y
        while (tempX - 1 >= 0 and tempY - 1 >= 0):
            if(table[tempX - 1][tempY - 1] == 'Q'):
                return False
            tempX -= 1
            tempY -= 1
        tempX = x
        tempY = y
        while (tempX -1 >= 0 and tempY + 1 <= len(table)-1 ):
            if(table[tempX - 1][tempY + 1] == 'Q'):
                return False
            tempX -= 1
            tempY += 1
        return True


