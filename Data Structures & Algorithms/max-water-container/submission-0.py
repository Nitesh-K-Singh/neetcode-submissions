class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #brute force
        # select any index i, j in heights
        # ans: min(heights(i), heights(j))*abs(j-i)
        # iterate over all pairs and return max

        n = len(heights)
        max_area = 0
        for i in range(n):
            for j in range(i+1,n):
                area = (j-i)*min(heights[i], heights[j])

                if area>max_area:
                    max_area = area

        
        return max_area