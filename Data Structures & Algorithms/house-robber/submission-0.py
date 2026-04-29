class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        
        V = [nums[0], max(nums[0], nums[1])]

        for i in range(2,n):
            v = max(nums[i]+V[0], V[1])
            V[0] = V[1]
            V[1] = v

        return v
            
        