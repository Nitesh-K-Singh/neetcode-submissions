class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force O(N^2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # hash map
        n = len(nums)
        # short = [target]*n - nums
        shorts = [target - num for num in nums]
        store = {}
        for i in range(n):
            store[nums[i]] = i

        for i in range(n):
            short = shorts[i]
            if short in store.keys():
                value = store.get(short)
                return [i,value]



        