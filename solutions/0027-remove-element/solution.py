class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0
        nums_len = len(nums)
        removed_elements = 0

        while i < nums_len: 
            if nums[i] == val: 
                nums.pop(i)
                nums_len -= 1
                removed_elements += 1
            else:
                i += 1

        return len(nums)
