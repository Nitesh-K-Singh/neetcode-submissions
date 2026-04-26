class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        # store values for each cell
        matrix = [[0]*n for _ in range(m)]

        # base cases
        matrix[m-1] = [1]*n #last row ones

        for i in range(m):   # last column ones
            matrix[i][n-1] = 1
        
        # bottoms up

        for i in range(m-2,-1, -1):
            for j in range(n-2,-1,-1):
                matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]

        return matrix[0][0]

    

    



        