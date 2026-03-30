class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer-moore voting https://www.geeksforgeeks.org/theory-of-computation/boyer-moore-majority-voting-algorithm/
        
        res = nums[0]
        votes = 1 
        for i in range(1, len(nums)):
            num = nums[i]
            if num != res: 
                votes -= 1 
                if votes <= 0: 
                    res = num
                    votes = 1 
            else: 
                votes += 1 
        return res 
