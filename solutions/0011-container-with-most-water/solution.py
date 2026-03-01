class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        output = 0 

        while l < r: 
            tmp = min(height[l], height[r]) * (r - l)
            output = max(output, tmp)

            if height[l] > height[r]: 
                r -= 1 
            else: 
                l += 1 
        
        return output
