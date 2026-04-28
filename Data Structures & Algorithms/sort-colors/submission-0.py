class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = {}

        for i in nums:
            counts[i] = counts.get(i,0) + 1

        result = [0]*counts.get(0, 0) + [1]*counts.get(1, 0) + [2]*counts.get(2, 0)
        nums[:] = result
        return result
        