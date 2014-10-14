class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if (m < 1):
            for i in range(len(B)):
                A[i] = B[i]
            return
        if (n < 1):
            return
        indexB = 0
        aLength = m
        for i in range(n + m - 1):
            if (B[indexB] < A[i]):
                A.insert(i, B[indexB])
                indexB += 1
                aLength += 1
            else:
                if (i == aLength -1):
                    A.insert(i+1, B[indexB])
                    indexB += 1
                    aLength += 1
            if ( indexB >= n):
                return

