class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # approach
        # for any n in nums: subproblem- solve two sum with target -n
        # two sum: maintain a dictionary and solve
        # lets cleanly implememnt two sum first


        def two_sum(input: list[int], target: int) -> list[int]:


            n = len(input)
            result = []
            value = {}

            for i in range(n): 

                if target - input[i] in value.keys():
                    result.append([input[i],target - input[i]]) # changed it to return numbers instead of indices
                value[input[i]] = i

            return result

        final_result = []
        for i in range(len(nums)):
            pairs = two_sum(input = nums[i+1:],target = -nums[i] )
            
            for pair in pairs:
                final_result.append([nums[i]] + pair)

            # if len(result) == 3:
            #     final_result.append(result)

        return final_result

