class Solution:
    # @return an integer
    def romanToInt(self, s):
        if (s == None):
            return None
        
        counter = 0
        currentNum = 0
        lastNum = 0
        charNum = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        for i in range(len(s)):
            index = len(s)-1-i  #start from right
            currentNum = charNum.get(s[index])
            if (currentNum == None):
                return None
                
            if (lastNum == 0):
                lastNum = currentNum
                counter += currentNum
                currentNum = None
                continue
            
            if (currentNum != lastNum):
                if (max(currentNum, lastNum) == lastNum):
                    counter -= currentNum
                    lastNum = currentNum
                    currentNum = None
                    continue
                    
                if (max(currentNum, lastNum) == currentNum):
                    counter += currentNum
                    lastNum = currentNum
                    currentNum = None
                    continue
                    
            if (currentNum == lastNum):
                counter += currentNum
                currentNum = None
                continue
            
        return counter
                
