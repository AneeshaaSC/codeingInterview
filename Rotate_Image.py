class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        if (len(matrix) <= 1 and len(matrix[0])<=1):
            return matrix
        for x in range(len(matrix)/2):
            y = x
            while(y<n-1-x):
                matrix[y][len(matrix)-1 - x],matrix[len(matrix)-1 - x][len(matrix)-1 - y],matrix[len(matrix)-1 - y][x]    ,matrix[x][y] =  matrix[x][y], matrix[y][len(matrix)-1 - x],matrix[len(matrix)-1 - x][len(matrix)-1 - y], matrix[len(matrix)-1 - y][x]    
                y += 1
        return matrix
