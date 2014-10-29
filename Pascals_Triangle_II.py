class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if (rowIndex < 1):
            return [1]
        if (rowIndex == 1):
            return [1,1]

        tempArray = [1]
        currentIndex = 1
        return self.help(tempArray, currentIndex, rowIndex)
        
    def help(self, tempArray, currentIndex, rowIndex):
        temp = []
        for i in range(len(tempArray)+1):
            if (i == 0):
                temp.append(1)
                continue
            if(i == len(tempArray)):
                temp.append(1)
                break
            
            temp.append(tempArray[i-1]+tempArray[i])
        if( currentIndex == rowIndex):
            return temp
        else:
            return self.help(temp, currentIndex+1, rowIndex)
            
        
        
