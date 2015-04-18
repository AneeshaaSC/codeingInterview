class Solution:
    # @param n, an integer
    # @return a string
    def countAndSay(self, n):
        if (n < 1):
            return None
        if (n == 1):
            return '1'
        else:
            lastString = self.countAndSay(n-1)
            tempString = ""
            currentNumber = '0'
            currentTimes = 0
            for i in range(len(lastString)):
                if (lastString[i] != currentNumber):
                    if (currentTimes != 0 ):
                        tempString += str(currentTimes) + currentNumber
                    currentNumber = lastString[i]
                    currentTimes = 1
                else:
                    currentTimes += 1
            tempString += str(currentTimes) + currentNumber
            return tempString
