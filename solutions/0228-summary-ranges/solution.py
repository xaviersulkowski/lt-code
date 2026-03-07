class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0

        while i < len(nums): 
            start = nums[i]
            while i < len(nums) - 1 and nums[i + 1] - nums[i] == 1: 
                i += 1 
            
            if start == nums[i]: 
                ranges.append(f"{nums[i]}")
            else: 
                ranges.append(f"{start}->{nums[i]}")
            
            i += 1 
        
        return ranges
