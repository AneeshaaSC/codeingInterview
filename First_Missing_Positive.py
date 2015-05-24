class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if (len(nums) < 1):
            return 1
        max = -9999999
        min = 9999999
        nums = list(set(nums))
        for i in nums:
            if (i<0):
                continue
            if (i > max):
                max = i
                
            if (i < min):
                min = i
        if(min > 1):
            return 1
        if(min < 0):
            min = 0
        bit = 0
        for i in range(max):
            bit = bit |(1 << i)

        for i in nums:
            if (i<=0):
                continue
            bit = bit ^ (1 << i-1)

        if(bit == 0):
            return max + 1
        else:
            for result in range(1,max+1):
                if ((bit & (1 << result-1)) != 0):
                    return result 


