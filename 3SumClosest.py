class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        closest = 999999999
        for i in range(len(num)-2):
            j = i+1
            k = len(num) - 1
            while(j < k):
                if ( abs(target - num[i] - num[j] - num[k]) < abs(target - closest) ):
                    closest = num[i] + num[j] + num[k]
                if (num[i] + num[j] + num[k] > target):
                    k -= 1
                elif (num[i] + num[j] + num[k] < target):
                    j += 1
                else:
                    return num[i] + num[j] + num[k]
                    
        return closest
