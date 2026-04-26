class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # # Approach using division and handling zeroes
        # # find total non-zero product once
        # # if numb 0 >= 2: all zero
        # # if num 0 = 1, 0 case
        # # handle edge case 0

        # total_product = 1
        # for i in nums:
        #     if i !=0:
        #         total_product = i*total_product

        # zeroes = [i for i in range(len(nums)) if nums[i]==0]
        # if len(zeroes) > 1:
        #     return [0]*len(nums)

        # if len(zeroes) == 0:
        #     return [int(total_product/num) for num in nums]

        # if len(zeroes) == 1:
        #     result = [0]*len(nums)

        #     result[zeroes[0]] =  total_product

        #     return result
            


        # return result

        # using prefix, postfix

        prefix = [1]*len(nums)
        for i in range(len(nums)):
            if i-1>=0:
                prefix[i] = prefix[i-1]*nums[i-1] 
        
        postfix = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i+1 <= len(nums)-1:
                postfix[i] = postfix[i+1]*nums[i+1]

        result = []
        for i in range(len(nums)):
            result.append(prefix[i]*postfix[i])

        
        return result



        