class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Approach
        # find total product once
        # do total_product/number
        # handle edge case 0

        total_product = 1
        for i in nums:
            if i !=0:
                total_product = i*total_product

        zeroes = [i for i in range(len(nums)) if nums[i]==0]
        if len(zeroes) > 1:
            return [0]*len(nums)

        if len(zeroes) == 0:
            return [int(total_product/num) for num in nums]

        if len(zeroes) == 1:
            result = [0]*len(nums)

            result[zeroes[0]] =  total_product

            return result
            



    

        return result



        