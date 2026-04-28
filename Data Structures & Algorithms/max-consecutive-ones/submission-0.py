class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        n = len(nums)

        g = 0
        l = 0
        for i in range(n):
            if nums[i] == 1:
                l = l + 1
                g = max(l,g)
            else:
                # g = max(l,g)
                l = 0
        
        return g

        