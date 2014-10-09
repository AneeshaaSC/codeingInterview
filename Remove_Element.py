class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if(len(A) < 1):
            return 0
        while(True):
            if elem in A:
                A.remove(elem)
            else:
                return len(A)
