ass Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        for i in range(len(gas)):
            cost[i] = gas[i] - cost[i]
        if (sum(cost) <0):
            return -1
        if (len(gas) <= 1):
            return 0
        for index in range(len(gas)):
            if (cost[index] > 0 ):
                break
            
        i = (index + 1 )%len(gas)
        gasLeft = cost[index]
        
        while(1):
            gasLeft += cost[i]
            if (i == index):
                return index
            if (gasLeft >= 0):
                i += 1
                i = i % len(gas)
                
            else:
                index = (i + 1) % len(gas)
                i = (index + 1) % len(gas)
                gasLeft = cost[index]
                
