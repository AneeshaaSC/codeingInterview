class Solution:
    # @return a boolean
    def isValid(self, s):
        if (len(s) <= 1):
            return False
        check = 0
        stack=[]

        #check = total number
        i = 0
        while(i< len(s) ):
            if (s[i] == '(' ):
                check += 1
                stack.append(')')
                
            if (s[i] == '['):
                check += 1
                stack.append(']')
                
            if (s[i] == '{' ):
                check += 1
                stack.append('}')     
                
            if (s[i] == ')'):
                if (len(stack) < 1):
                    return False
                temp = stack.pop()
                if (s[i] != temp):
                    return False
                check -= 1
                
            if (s[i] == ']'):
                if (len(stack) < 1):
                    return False
                temp = stack.pop()
                if (s[i] != temp):
                    return False
                check -= 1
                
            if (s[i] == '}'):
                if (len(stack) < 1):
                    return False
                temp = stack.pop()
                if (s[i] != temp):
                    return False
                check -= 1
                
            if(check <0):
                return False
            i+=1
            
        if (check != 0):
            return False
        else:
            return True
            
