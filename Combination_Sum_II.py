class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.helper(candidates, target,[], result)
        answer = []
        for i in result:
            if not i in answer:
                answer.append(i)
        return answer
        
        
        
    def helper(self, array, target, current, result):
#        temp = current[::]
        for index,value in enumerate(array):
            if(target - value > 0 ):
    
                self.helper(array[index+1::], target - value, current + [value], result)
                
            if(target - value == 0):
                result.append(current + [value])
                
            if(target - value <0):
                return 
        
