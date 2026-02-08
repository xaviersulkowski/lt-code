class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r: 
            tmp_res = (r - l) * min(height[l], height[r])
            res = max(res, tmp_res)
            if height[l] > height[r]:
                r -= 1
            else: 
                l += 1
        return res 
            
