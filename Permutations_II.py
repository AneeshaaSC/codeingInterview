class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}

    def permuteUnique(self, nums):
        number = []
        self.helper(nums,[],number)
        return number
        
    def helper(self, nums, result,number):
        if(result == []):
            for i in range(len(nums)):
                rest = nums[0:i]+nums[i+1::]
                rest.sort()
                temp = [ [nums[i]] ,rest]
                if (temp not in result):
                    result.append(temp)
            self.helper(nums,result,number)
        else:
#            print result
            temp = []
            for value in result:
                if(len(value[1]) <1):
                    number.append( value[0])
                else:
                    for index in range(len(value[1])):
                        add = [value[0]+[value[1][index]],value[1][0:index] + value[1][index+1::]]
                        if (add not in temp):
		            temp.append(add)
            if(temp != []):
	        self.helper(nums,temp,number)
