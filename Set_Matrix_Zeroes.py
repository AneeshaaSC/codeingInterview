
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if(len(matrix) < 1):
            return matrix
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if (matrix[x][y]) == 0:
                    for i in range(len(matrix)):
                        if (matrix[i][y] !=0 ):
                            matrix[i][y] = None
                        
                    for i in range(len(matrix[0])):
                        if (matrix[x][i] != 0):
                            matrix[x][i] = None                   
                
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if (matrix[x][y] == None):
                    matrix[x][y] = 0
        return matrix
