class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if(len(obstacleGrid)<1):
            return 0
        if(len(obstacleGrid)==1 and len(obstacleGrid[0])==1):
            if (obstacleGrid[0][0] == 0):
                return 1
            else:
                return 0

        for x in range(len(obstacleGrid)):
            for y in range(len(obstacleGrid[0])):
                if (x==0 and y==0):
                    obstacleGrid[x][y] = 1 - obstacleGrid[x][y]
                    continue 
                if (obstacleGrid[x][y] == 0):
                    if(x == 0):
                        obstacleGrid[x][y] =  obstacleGrid[x][y-1]
                        continue
                    if(y == 0):
                        obstacleGrid[x][y] = obstacleGrid[x-1][y]
                        continue
                    obstacleGrid[x][y] = obstacleGrid[x-1][y] + obstacleGrid[x][y-1]
                    continue 

                
                if (obstacleGrid[x][y] == 1):
                    obstacleGrid[x][y] = 0
                    
            
        
        return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
        
