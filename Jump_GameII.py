class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if(len(nums) <= 1):
            return 0
        for index,value in enumerate(nums):
    		nums[index] = value + index
    	i = 0
    	times = 1
    	while(1):
    		if(nums[i]>=len(nums)-1):
    			return times
    		couldReach = nums[i+1:nums[i]+1]
    		maxValue = max(couldReach)
    		i = couldReach.index(maxValue) + i + 1
    		times += 1

    		




