class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # bottom up  DP
        # start = (0,0)
        # choice at each step : down, right
        # so traverse row wise
        # maintain count of bad path -- anything that hits 1
        # total - bad path = answer

        grid = obstacleGrid.copy()
        m = len(grid)
        n = len(grid[0])
        
      

        paths = [[0 for _ in range(n)] for _ in range(m) ]
        paths[0][0] = 1
        

        for i in range(m):
            for j in range(1,n):
                if i >= 1:
                    left = paths[i-1][j]
                else: 
                    left = 0
                if j >= 1:
                    up = paths[i][j-1]
                else:
                    up = 0

                paths[i][j] = left*(1- grid[i-1][j]) + up*(1- grid[i][j-1])
        
        return paths[m-1][n-1]
