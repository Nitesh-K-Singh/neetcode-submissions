class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #brute force O(n^2), O(1)
        # [-2,1]
        n = len(nums)
        g_sum = nums[0]
        for i in range(n):  
            l_sum = nums[i] 
            # g_sum = max(l_sum, g_sum)

            for j in range(i+1,n): 
                l_sum = l_sum + nums[j] 
                g_sum = max(l_sum, g_sum) 
            
            g_sum = max(l_sum, g_sum)
            

        return g_sum




        