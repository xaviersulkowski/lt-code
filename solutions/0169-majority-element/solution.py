class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer-moore voting https://www.geeksforgeeks.org/theory-of-computation/boyer-moore-majority-voting-algorithm/
        
        res = nums[0]
        count = 1 
        for i in range(1, len(nums)): 
            if nums[i] == res: 
                count += 1 
            else: 
                count -= 1 
                if count <= 0: 
                    res = nums[i]
                    count = 1
        
        return res
