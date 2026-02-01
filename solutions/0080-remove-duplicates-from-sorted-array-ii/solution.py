class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0

        current = None 
        count = 0 
        k = 0 
        for i in range(len(nums)): 
            if nums[i] == current: 
                count += 1 
            else: 
                current = nums[i]
                count = 1 

            if count <= 2: 
                nums[k] = current 
                k += 1 

        return k
