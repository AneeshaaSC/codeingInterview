class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if (n == 0):
            return 1
        if (n < 0):
            return 0
            
        return self.helperFun(n)
    
        
    def helperFun(self, n, index=2, currentResult=2, lastResult=1):
        if (n == 1):
            return 1
        if (n == 2):
            return 2

        while (True):
            temp = currentResult
            currentResult = temp + lastResult
            lastResult = temp
            index += 1
            if (index ==n):
                return currentResult

            
