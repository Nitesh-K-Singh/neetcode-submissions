class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # ineffciency in brute force -- going over same computation again and again
        # effcient: track back from last element.. store sum of subarrays from last to first
        # maintain a global max

        n = len(nums)
        # g_max = 0
        # l_max = 0
        g_max = nums[-1]
        l_max = nums[-1]
        for i in range(n-2,-1,-1):
            l_max = max(l_max + nums[i], nums[i])
            g_max = max(l_max, g_max)

        return g_max




        #brute force O(n^2), O(1) 

        # n = len(nums)
        # g_sum = nums[0]
        # for i in range(n):  
        #     l_sum = nums[i] 

        #     for j in range(i+1,n): 
        #         l_sum = l_sum + nums[j] 
        #         g_sum = max(l_sum, g_sum) 
            
        #     g_sum = max(l_sum, g_sum)
            

        # return g_sum




        