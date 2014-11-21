ass Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if(len(strs) ==1):
            return strs[0]
        if(len(strs) <1):
            return ""
        common = strs[0]
        for i in range(len(strs)):
            if (common in strs[i][0:len(common)]):
                continue
            else:
                while(True):
                    if (common == ""):
                        return ""
                    if (common in strs[i][0:len(common)]):
                        break
                    else:
                        common = common[0:len(common)-1]
        if(len(common) < 1):
            return ""
        else:
            return common
                    
                
                
                
