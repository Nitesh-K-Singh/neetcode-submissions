class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # approach: two pointers
        # i = 0, j = n-1
        # if sum > target  decrease j
        # if sum < target  increase i
        # if sum == target return
        # so this is one pass only
        # but what about if there are multiple solutions? Is one pass still enough?

        n = len(numbers)
        left , right = 0, n-1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [numbers[left], numbers[right]]
            
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            
            elif numbers[left] + numbers[right] > target:
                right = right - 1

        
        return "no pair found"
            


        
        