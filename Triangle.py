class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if(len(triangle) <1):
            return None
        lastRow = triangle[0]
        for x in range(1,len(triangle)):
            temp = ["" for  z in range(x+1)]
            
            for y in range(len(lastRow)):
                temp[y] = lastRow[y] + triangle[x][y] if temp[y] == "" else min(temp[y], lastRow[y] + triangle[x][y])
                temp[y+1] = lastRow[y] + triangle[x][y+1] if temp[y] == "" else min(temp[y+1], lastRow[y] + triangle[x][y+1])
                
            lastRow = temp
        return min(lastRow)
                                    
                            
