class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if(A == None or A == []):
            return 0
        mark = [None,0]
        result = 0
        for index, value in enumerate (A):
            if (value != mark[0]):
                mark[0] = value
                mark[1] = 1
                result += 1
                continue 
            elif(mark[1] == 1):
                mark[1] += 1
                result += 1
                continue 
            elif(mark[1] == 2):
                A[index] = None
                continue
        for i in range(A.count(None)):
            A.remove(None)
        return result

