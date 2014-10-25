class Solution:
    # @return an integer
    def maxArea(self, height):
        if (len(height) < 1):
            return 0
        maxArea = 0
        i=0
        end = len(height) - 1
        while (True):
            if (i == end):
                break
            if (height[end] >= height[i]):
                maxArea = max(maxArea, (end-i)*height[i])
                i+=1
                continue
            if (height[i] > height[end]):
                maxArea = max(maxArea, (end-i)*height[end])
                end-=1
                continue
        return maxArea
                
