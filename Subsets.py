class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if (len(S) < 1):
            return S
        if (len(S) == 1):
            temp = []
            temp.append(S)
            temp.append([])
            return temp
        S.sort()
        temp = self.helper(S)
        temp.append([])
        return temp
        
        
    def helper(self, array):
        if (len(array) == 1):
            return [array]
            
        result = []
        for i in range(len(array)):
            result.append([array[i]])
            temp = self.helper(array[i+1::])
            if (temp != []):
                for x in temp:
                    x.insert(0,array[i])
                    result.append(x)

        return result                
            
