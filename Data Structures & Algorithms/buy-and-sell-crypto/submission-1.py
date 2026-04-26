class Solution:
    def maxProfit(self, prices: List[int]) -> int:


      #   prices = [10,1,5,6,7,1]
      #  max_future_price, start backwards = [7,7,7,7,1,0]

        n = len(prices)
        max_future_price = 0
        max_profit = 0
        for i in range(n-2, -1, -1):
            max_future_price = max(prices[i+1], max_future_price )
            max_profit = max(max_future_price - prices[i], max_profit)

        return max_profit
    
    
    








        # brute force
        # pick any i, j , j>i
        # profit = prices[j] - prices[i]
        # O(n^2), O(1)

        # n = len(prices)
        # max_profit = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         max_profit = max(max_profit, prices[j] - prices[i])

        
        # return max_profit


        