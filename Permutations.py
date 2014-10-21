class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if (len(num) <= 1):
            return [num]
        return self.permutation(num)
        
    def permutation(self, array):
        if (len(array) == 1):
            return [array]
        result = []
        for i in range(len(array)):
            temp = array[i]
            tempArray = self.permutation(array[0:i] + array[i+1::])
            for x in tempArray:
                x.insert(0,temp)
                result.append(x)
        return result 
                
