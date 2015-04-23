class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if (target % 2 == 0):
            result = []
            if( num.count(target / 2) >= 2):
                result.append(num.index(target / 2) + 1)
                result.append(num[result[0]::].index(target / 2) + result[0] + 1)
                return result
        result = []
        dict = {}
        for i in num:
            dict.update({i:1})
        for i in num:
            if (dict.get(target - i) == 1):
		if(target % 2 == 0 and target / 2 == i):
			continue
                result.append(i)
                result.append(target - i)
		break
        for i in range(len(result)):
            result[i] = num.index(result[i]) + 1
        return result
