class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        votes = 1

        for i in range(1, len(nums), 1): 
            n = nums[i]

            if n == candidate: 
                votes += 1 
            else: 
                votes -= 1 
                if votes == 0: 
                    candidate = n 
                    votes += 1 
        
        return candidate

