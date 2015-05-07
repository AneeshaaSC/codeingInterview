class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if (target not in nums):
            return -1
        else:
            for index,value in enumerate (nums):
                if(value == target):
                    return index
