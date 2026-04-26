class Solution:
    def findMin(self, nums: List[int]) -> int:

        # trivial: O(n)

        min = nums[0]
        for n in nums:
            if n < min:
                min = n

        return min
        