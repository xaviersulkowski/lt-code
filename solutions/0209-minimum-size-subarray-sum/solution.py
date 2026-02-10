class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        min_size = float("inf")

        for r in range(len(nums)): 
            total += nums[r]
            if total >= target:
                while total >= target: 
                    min_size = min(min_size, r - l + 1)
                    total -= nums[l]
                    l +=1 
        
        return 0 if min_size == float("inf") else min_size
