class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input 
        # [1, 2, 3, 4]

        # init output
        # [1, 1, 1, 1]
        
        # prefixes
        # [1, 1, 2, 6]

        # output left to right multiplied with prefixes
        # [1, 1, 2, 6]

        # postfixes 
        # [1, 4, 12, 24] (right to left)
        
        # output right to left multiplied with postfixes
        # [24, 12, 8, 6]

        output = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)): 
            output[i] *= prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= postfix 
            postfix *= nums[i]

        return output
