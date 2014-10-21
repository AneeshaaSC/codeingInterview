class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if (len(A) <= 1):
            return A
        length = len(A)
        numberOfZero = 0
        numberOfTwo = 0

        i = 0
        while(i < length - numberOfTwo ):
            if (A[i] == 0):
                del(A[i])
                A.insert(0,0)
                numberOfZero += 1
                i+=1

                
            elif (A[i] == 1):
                A.remove(1)
                A.insert(numberOfZero,1)
                i+=1
            
            elif (A[i] == 2):
                A.remove(2)
                A.append(2)
                numberOfTwo += 1
