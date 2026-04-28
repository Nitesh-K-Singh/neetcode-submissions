class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # return [x for x in nums if x != val]

        # two pointers

        i = 0

        for num in nums:
            if num != val:
                nums[i] = num
                i = i + 1

        return i
