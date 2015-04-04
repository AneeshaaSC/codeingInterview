class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if (not s):
            return s
        output = []
        temp = []
        self.findPartition(s,output,temp)
        return output
        
    def findPartition(self, s, output, temp):
        if (not s):
            output.append(temp[:])
            return
        
        for i in range(1,len(s)+1):
            if (self.isPalindrome(s[:i])):
                temp.append(s[:i])
                self.findPartition(s[i::], output,temp)
                temp.pop()
        
        
        
    def isPalindrome(self, string):
        if (string == string[::-1]):
            return True
        else:
            return False
