class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a_int = 0
        for i in range(len(a))[::-1]:
            a_int += int(a[i]) * pow(2,len(a) - i- 1)
	b_int = 0
        for i in range(len(b))[::-1]:
            b_int += int(b[i]) * pow(2,len(b) - i- 1)
	result_int = a_int + b_int
	return bin(result_int)[2::]
