class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # # two pass
        # result = []

        # for i in range(n):
        #     result.append(nums[i])

        # for i in range(n,2*n):
        #     result.append(nums[i-n])

        # return result

        #one pass

        result = [0]*(2*n)
        for i in range(n):
            result[i] = nums[i]
            result[n+i] = nums[i]

        return result



        