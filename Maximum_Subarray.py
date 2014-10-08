class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if (len(A) < 1):
            return 0
        if (len(A) == 1):
            return A[0]
        result = A[0]
        currentSum = A[0]
        for i in range(len(A)):
            if (i == 0):
                continue

            temp = currentSum + A[i]

            if (temp >= A[i]):
                currentSum = temp
            else:
                currentSum = A[i]

            if (currentSum > result ):
                result = currentSum
        return result
