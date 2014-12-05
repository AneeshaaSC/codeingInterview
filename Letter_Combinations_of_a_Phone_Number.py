ass Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if(len(digits)<1):
            return [""]
        result = []
        for i in range(len(digits)):
            if (result == []):
		for x in self.returnString( digits[i] ):
                    result.append(x)
            else:
                temp = []
                for x in result:
                    for y in self.returnString( digits[i] ):
                        temp.append(x+y)
                result = temp
        return result 
            
            
    def returnString (self, inputs):
        if (inputs == "0"):
            return " "
        if (inputs == "1"):
            return ""
        if (inputs == "2"):
            return "abc"
        if (inputs == "3"):
            return "def"
        if (inputs == "4"):
            return "ghi"
        if (inputs == "5"):
            return "jkl"
        if (inputs == "6"):
            return "mno"
        if (inputs == "7"):
            return "pqrs"
        if (inputs == "8"):
            return "tuv"
        if (inputs == "9"):
            return "wxyz"


