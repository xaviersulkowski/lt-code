class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 

        area = 0
        while left != right: 
            
            len_ = right - left 
            height_ = min(height[left], height[right])
            area_ = len_ * height_ 

            area = max(area, area_)

            if (height[left] < height[right]):
                left += 1
            else: 
                right -= 1

        return area


