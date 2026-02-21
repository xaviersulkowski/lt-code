class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums) 
        n = len(nums)
        
        # reverse entire array 
        l, r = 0, n - 1
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1

        # reverse first part
        l, r = 0, k - 1
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1

        # reverse second part
        l, r = k, n - 1
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1
