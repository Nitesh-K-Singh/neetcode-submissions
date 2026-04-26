class Solution:
    def climbStairs(self, n: int) -> int:

        if n <=2:
            return n

        values = [0]*n
        values[n-1]  = 1
        values[n-2] = 2

        for i in range(n-3, -1, -1):
            values[i] = values[i+1] + values[i+2]

        return values[0]
        
        