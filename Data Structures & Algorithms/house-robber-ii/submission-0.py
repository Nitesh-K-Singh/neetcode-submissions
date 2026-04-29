class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_linear(seq):

            n = len(seq)
            if n == 1:
                return seq[0]

            if n == 2:
                return max(seq)

            
            base_value = [seq[0], max(seq)]
            i = 2
            while i in range(2,n):
                value = max(seq[i]+base_value[0], base_value[1])
                base_value = [base_value[1], value]
                i = i + 1

            return value



        linear_nums = [nums[1:], nums[:-1]]
        value = [rob_linear(x) for x in linear_nums]

        return max(value)
        


        

    
        
        
        