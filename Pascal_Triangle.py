class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if (numRows < 1):
            return []
        if (numRows == 1):
            return [[1]]
        
        result = []
        result.append([1])
        for i in range(1,numRows):
            result.append([])
            for x in range(len(result[i-1]) +1 ):
                if(x == 0 ):
                    result[i].append(1)
                    continue
                if( x == len( result[i-1] ) ) :
                    result[i].append(1)
                    continue                    
                else:
                    result[i].append(result[i-1][x]+result[i-1][x-1])
        return result
