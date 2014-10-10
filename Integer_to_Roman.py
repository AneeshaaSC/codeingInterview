class Solution:
    # @return a string
    def intToRoman(self, num):
        if (num == None):
            return ''
        if (num < 0):
            return ''

        result = ""
        charNum = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        if(charNum.has_key(num)):
            return charNum.get(num)
        tempAround = self.roundNum(num)
        while (num > 0):
            if(charNum.has_key(num)):
                result = result + charNum.get(num)
                return result
            if (charNum.has_key(tempAround)):
                result = result + charNum.get(tempAround)
                num -= tempAround
                tempAround = self.roundNum(num)
            else:
                tempAround -= self.minus(num)
                
                
                
    def roundNum(self,num):
        if num > 1000:
            num = num /1000 *1000
            return num
        if num > 100:
            num = num /100 * 100
            return num
        if num > 10:
            num = num /10 *10
            return num
            
    def minus(self,num):
        if num > 1000:
            return num - num % 1000 - 1000
            
            
        if num > 100:
            value = num - num % 100 - 100
            if (value >= 500 ):
                return 100
            else:
                return value

        if num > 10:
            value = num - num % 10 - 10 
            if (value >= 50 ):
                return 10
            else:
                return value
        


