class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if(len(S) < 1 or len(T) < 1):
            return 0
        table = [[0 for i in range(len(S) + 1) ] for i in range(len(T) + 1)]
        for x in range(len(T) + 1):
            for y in range(x,len(S)+1):
                if(x == 0 or y == 0):
                    continue
                s = y - 1
                t = x - 1
                if (T[t] == S[s]):
                    table[x][y] =  table[x-1][y-1] + table[x][y-1] 
                    if (x == 1):
                        table[x][y] += 1
                else:
                    table[x][y] = table[x][y-1]
        return table[len(table)-1][len(table[0])-1]
