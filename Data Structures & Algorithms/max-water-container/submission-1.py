class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # two pointers
        n = len(heights)

        left = 0
        right = n-1

        max_area = (right-left)*min(heights[left], heights[right])

        while right > left:
            area = (right-left)*min(heights[left], heights[right])
            if area > max_area:
                max_area = area
            
            if heights[left]<= heights[right]:
                left = left + 1
            
            elif heights[left] > heights[right]:
                right = right - 1

        return max_area
            


            



        
        #brute force
        # select any index i, j in heights
        # ans: min(heights(i), heights(j))*abs(j-i)
        # iterate over all pairs and return max
        # O(n^2)

        # n = len(heights)
        # max_area = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         area = (j-i)*min(heights[i], heights[j])

        #         if area>max_area:
        #             max_area = area

        
        # return max_area