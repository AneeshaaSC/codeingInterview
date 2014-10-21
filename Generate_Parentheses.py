class Solution:
    # @param an integer
    # @return a list of string
    result=[] 
    def generateParenthesis(self, n):
        if (n<1):
            return []
	self.result = []
        self.parentheses([],0,n,n)
        return self.result
        
    def parentheses(self,currentResult,count,left,right):
        if (left == 0 and right == 0 and count == 0):
            self.result.append(''.join(currentResult))
            return
        if (count < 0):
            return
        if (left >0):    
        	self.parentheses(currentResult + ['('],count + 1 ,left-1,right)
	if(right>0):
        	self.parentheses(currentResult + [')'],count - 1 ,left,right-1)

b=Solution()
print b.generateParenthesis(2)
