class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if (x == 1):
            return x

        if (x == 0):
            return 0
            
        if (n == 0):
            return 1
            
        if (n < 0):
            x = 1/x
            n = -n
            
        power = 1
        temp = x
        array = []
        array.append([power, temp])
        while (power * 2 < n):
            array.append([power*2, temp*temp])
            if ( abs(temp) <= abs (1e-15) ):
                return 0
            temp = temp * temp
            power *= 2
        if ( n > power):
            temp *= pow(x, n - power)
            
        return temp
         
        

