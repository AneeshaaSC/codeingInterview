class Solution:
    # @return a string
    def intToRoman(self, num):
        if (s == None):
            return None
   
        result = ""
        charNum = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VII',9:'IX',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        if(char_Num.has_key(num)):
            return char_Num.get(num)
        tempAround = num
        while (True):
            tempAround = tempAround % 10 *10
            if (char_Num.get(tempAround)):
                result = result + char_Num.get(tempAround)
                tempAround
            else:
                
  

