class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        # rotate array 
        l = 0 
        r = len(nums) - 1 
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1 
        
        # rotate left side 
        l = 0 
        r = k - 1
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1 

        # rotate right side 
        l = k 
        r = len(nums) - 1 
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1 
