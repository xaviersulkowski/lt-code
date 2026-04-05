class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1 
        areaMax = 0 

        while l < r: 
            numL = height[l]
            numR = height[r]

            area = (r - l) * min(numL, numR)
            areaMax = max(area, areaMax)

            if numL > numR: 
                r -= 1 
            else: 
                l += 1 

        return areaMax

        
