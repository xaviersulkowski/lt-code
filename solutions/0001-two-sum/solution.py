class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)): 
            diff = target - nums[i]
            if lookup.get(diff) is not None: 
                return [i, lookup.get(diff)]
            else: 
                lookup[nums[i]] = i
        
