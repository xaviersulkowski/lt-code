class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) == 1):
            return [nums]

        results = []
        self.permute_(nums, 0, results)
        return results

    def permute_(self, nums, begin, results): 

        if (begin >= len(nums)): 
            results.append(nums[:])
            return

        for i in range(begin, len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.permute_(nums, begin+1, results)
            nums[begin], nums[i] = nums[i], nums[begin]
