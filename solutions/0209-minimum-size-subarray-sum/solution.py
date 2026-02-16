class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, res = 0, float('inf')
        l = 0 
        for r in range(len(nums)): 
            total += nums[r]
            while total >= target: 
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1 
        
        return 0 if res == float('inf') else res
