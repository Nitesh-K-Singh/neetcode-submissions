class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        min_coin_needed = [float('inf')]*(amount+1)
        min_coin_needed[0] = 0

        i = 1
        while i <= amount:
            valid = [min_coin_needed[i - x] for x in coins if x <= i]
            min_coin_needed[i] = 1 + min(valid) if valid else float('inf')
            
            i = i + 1

        if min_coin_needed[amount] == float('inf'):
            return -1
        else:
            return min_coin_needed[amount]
        