class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start = 0
        end = len(A) - 1
        i = end / 2
        index1=-1
        index2=-1
        while(True):
            if (end - start == 1):
                if (target != A[start] and target != A[end]):
                    return [-1,-1]
            
            if (target > A[i]):
                if (i == start):
                    i = end

                    continue
                if (i == end):
                    return [-1,-1]
                start = i   
                i = i + (end - start)/2
            
            
            if (target < A[i]):
                if(i == start):
                    return [-1,-1]
                if(i == end):
                    i = start

                    continue
                end = i
                i = i - (end - start) /2
            
            
            if(target == A[i]):
                index1=i
                index2=i
                break
            
            
        if(index1!=-1):
            
            while(A[index1] == target):
                index1 -= 1
                if (index1<0):
                    break
            index1 +=1
            
        if(index2!=-1):
            while(A[index2] == target):
                index2 += 1
                if (index2>len(A)-1):
                    break
            index2 -=1
        return[index1,index2]
            
        
