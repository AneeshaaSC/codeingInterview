class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if(len(grid) <1):
            return 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x==0 and y-1>=0):
                    grid[x][y] = grid[x][y] + grid[x][y-1]
                    continue
                if (y==0 and x-1>=0):
                    grid[x][y] = grid[x][y] + grid[x-1][y]
                    continue
                if (x!=0 and y!= 0):
                    grid[x][y] += min(grid[x-1][y],grid[x][y-1]) 
        return grid[len(grid)-1][len(grid[0])-1]
