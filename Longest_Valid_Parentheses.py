class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) < 2):
            return 0
        left = []
        zeros = [0 for i in s]
        zerosCheck = zeros[::]
        for index in range(len(s)):
            if (s[index] == "("):
                left.append(index)
            elif(s[index] == ")"):
                if(len(left) == 0):
                    continue
                else:    
                    zeros[left.pop()] = 1
                    zeros[index] = 1
        tempResult = 0
        result = 0
        print zeros
        for index in range(len(s) - 1):
            if(zeros[index] == 1 and zeros[index + 1] == 1):
                tempResult += 1
            else:
                result = max(result, tempResult)
                tempResult = 0
        result = max(result, tempResult)
        if(result % 2 == 1):
            result += 1
        return result
