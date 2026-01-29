class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_ptr, r_ptr = 0, 1
        profit = 0
        while r_ptr < len(prices): 
            if prices[r_ptr] < prices[l_ptr]: 
                l_ptr = r_ptr
            else: 
                profit = max(prices[r_ptr] - prices[l_ptr], profit)
            
            r_ptr += 1 

        return profit

