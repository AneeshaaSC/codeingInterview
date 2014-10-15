class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if( len(digits) < 1):
            return digits
        Range = range(len(digits))
        Range.reverse()
        offset = 0
        for i in Range:
            if ( i == len(digits) - 1 ):
                digits[i] += 1
            else:
                if (offset == 1):
                    digits[i] += offset
                    offset = 0
            if (i == 0 and digits[i] == 10):
                digits[i] = 0
                digits.insert(0,1)
                break
            
            if (digits[i] == 10):
                digits[i] = 0
                offset  = 1
        return digits
