class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = nums[0]
        votes = 1 
        
        for num in nums[1::]: 
            if num != element: 
                votes -= 1 
                if votes <= 0: 
                    element = num 
                    votes = 1
            else: 
                votes += 1 

        return element
