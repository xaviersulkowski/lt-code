class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # pointer at nums where to put the non-val value
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            i += 1

        return k

