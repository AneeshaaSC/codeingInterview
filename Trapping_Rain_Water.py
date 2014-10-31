class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if (len(A) < 3):
            return 0
        leftMax = A[0]
        rightMax = 0
        result = 0
        
        for i in A[2::]:
            rightMax = max(i,rightMax)
        for i in range(1,len(A)):
            if (leftMax > A[i] and rightMax > A[i]):
                result = result + min(leftMax, rightMax) - A[i]
            if (A[i] > leftMax):
                leftMax = A[i]
            if (A[i] == rightMax):
                rightMax = 0
                for x in A[i+1::]:
                    rightMax = max(x,rightMax)
        return result            
