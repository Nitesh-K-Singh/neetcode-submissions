class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # don't knwo whats brute force or whats optimal
        # can only think of on solution
        # also why is this even interesting? At ecah index there is no choice.. i must jump.
        # interesting problem would be if at each index i can choose to jump nums[i] or less.
        n = len(nums)
        state = 0
        while state < n-1:
            if nums[state] > 0:
                state = state + nums[state]
            else: 
                return state == n-1


        return state == n-1



        