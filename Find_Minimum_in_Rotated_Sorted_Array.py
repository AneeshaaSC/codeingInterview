import pdb
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if (len(num) == 1):
            return num[0]
        i=0
        end = len(num) -1
	if (num[i] < num[end]):
		return num[i]
        while(True):
#	    pdb.set_trace()
            mid = (i+end)/2
	    if(mid == i or mid == end):
		return min(num[i],num[end])
            if (i == end):
		return num[i]
	    if (num[i] > num[mid]):
		end = mid
	    elif (num[end] < num[mid]):
		i = mid

b=Solution()
print b.findMin([7,8,1,2,3,4,5,6])
