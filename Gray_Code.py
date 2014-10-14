class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if( n<= 0):
            return [0]
        result = self.BinaryGray(n)
        for i in range(len(result)):
            result[i] = int(result[i] ,2)
        return result


    def BinaryGray(self, n):
        if (n == 1):
            return ['0','1']
        
        temp = self.BinaryGray(n-1)
        temp1 = temp
        temp1.reverse()
        
        result = []
        for i in range(len(temp)):
            result.append('0'+ temp[i])
                
        for i in range(len(temp1)):
            result.append('1'+temp1[i])
        return result
