class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        cur_min = prices[0]

        for price in prices :

            max_profit = max(   price - cur_min , max_profit)
            cur_min = min(cur_min , price)
        
        return max_profit