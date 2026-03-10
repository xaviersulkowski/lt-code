class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # diff to i
        lookup = {}

        for i in range(len(nums)): 
            diff = target - nums[i]
            if diff in lookup: 
                return [i, lookup[diff]]
            else: 
                lookup[nums[i]] = i 

