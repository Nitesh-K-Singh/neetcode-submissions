class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # two pointers: 
        n = len(nums)
        nums_sorted = sorted(nums)
        result = {}
        # [-4,-1,-1, 0,1,2]
        for i in range(n):

            left, right = i+1, n - 1
            while right > left:
                sum = nums_sorted[left] + nums_sorted[right] 
                target =  -nums_sorted[i]
                if sum == target:
                    key = (nums_sorted[i], nums_sorted[left], nums_sorted[right])
                    result[key] = result.get(key,0) + 1
                    right = right - 1
                    left = left + 1
                
                elif sum < target:
                    left = left + 1

                elif sum > target:
                    right = right - 1
                
                

        return [x for x in result.keys()]


        







        
        # # approach
        # # for any n in nums: subproblem- solve two sum with target -n
        # # two sum: maintain a dictionary and solve
        # # lets cleanly implememnt two sum first


        # def two_sum(input: list[int], target: int) -> list[int]:


        #     n = len(input)
        #     result = []
        #     value = {}

        #     for i in range(n): 

        #         if target - input[i] in value.keys():
        #             result.append([input[i],target - input[i]]) # changed it to return numbers instead of indices
        #         value[input[i]] = i

        #     return result

        # final_result = []
        # for i in range(len(nums)):
        #     pairs = two_sum(input = nums[i+1:],target = -nums[i] )
    
        #     for pair in pairs:
        #         final_result.append([nums[i]] + pair)

        # # deduplicate
        # final_result_set = set(tuple(sorted(x)) for x in final_result)

        # return [list(x) for x in final_result_set]

