class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, p = 0, 1 
        profit = 0
        while p < len(prices):
            if prices[p] < prices[l]: 
                l = p 
            else: 
                profit = max(profit, prices[p] - prices[l])
            p += 1 
        return profit
