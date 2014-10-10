class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if (len(A) < 1 or len(A) == 1):
            return len(A)
        num = 1
        for i in range(1,len(A)):
            if(A[i]!=A[i-1]):
                A[num] = A[i]
                num += 1
        return num

