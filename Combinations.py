class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if(k > n):
            return range(1,n+1)
        if (k < 0 or n < 0):
            return []
        
        return self.helper(range(1,n+1), 1, k, [])
        
        
    def helper(self, array, currentK, k ,result):
#        if (currentK == k and currentK != 1):
#                return result
        tempArray = []       
        if(currentK == 1):
            for i in array:
                tempArray.append([i])
            result = tempArray    
            if (currentK == k):
                return result
            else:
                result = self.helper(array, currentK+1, k , result)
        else:
            for i in range (len(result)):
                for x in array[result[i][len(result[i])-1]::] :
                   tempArray.append(result[i]+[x])
            result = self.helper(array, currentK+1, k , tempArray)
        
        return result





            
        
