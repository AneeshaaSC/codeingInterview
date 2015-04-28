class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
	candidates.sort()
        result = []
        self.helper(candidates, target, result,[])
        return result
        
        
    def helper(self,candidates, target, result, temp):
	test = temp[::]
        for index,i in enumerate(candidates):
            if(target - i  >0):
                temp.append(i)
                self.helper(candidates[index::], target - i, result, temp)
	    	temp = test[::] 
            elif(target - i == 0):
                temp.append(i)
                result.append(temp)
                return
            elif(target - i< 0):
                return
        
a = Solution()
b=[8,7,4,3]
target = 7
print a.combinationSum(b,7)
