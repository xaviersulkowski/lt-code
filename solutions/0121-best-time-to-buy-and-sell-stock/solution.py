class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_ptr, r_ptr = 0, 1
        profit = 0

        while r_ptr < len(prices):
            tmp_profit = prices[r_ptr] - prices[l_ptr]
            if prices[r_ptr] < prices[l_ptr]:
                l_ptr = r_ptr
            else:
                profit = max(profit, tmp_profit)
            r_ptr += 1

        return profit

