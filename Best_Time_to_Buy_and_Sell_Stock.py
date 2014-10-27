class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if(len(prices)<2):
            return 0
        result = 0
        profit = []
        currentMax = 0
        for i in range(1,len(prices)):
            if (prices[i] > prices[i-1]):
                currentMax =currentMax + prices[i] - prices[i-1]
                result = max(result, currentMax)
            else:
                if(currentMax>0 and currentMax + prices[i] - prices[i-1] > 0):
                    profit.append(currentMax)
                currentMax = 0
            if (len(profit)>0):
                for x in range(len(profit)):
                    profit[x] = profit[x] + prices[i] -prices[i-1]
                    result = max(result, profit[x])
        return result
