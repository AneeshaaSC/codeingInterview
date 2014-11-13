class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if(len(A) <= 1):
            return True
        maxNum = 0
        for i in range(len(A)):
            maxNum = max(A[i] + i, maxNum)
            if (maxNum >= len(A)-1):
                return True
            if(i >= maxNum):
                return False 

