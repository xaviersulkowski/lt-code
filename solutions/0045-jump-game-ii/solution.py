class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l, r = 0, 0
        """
        l and r show the range of the array that is being processed by BFS, in step 0 only 0 index
        
        [2, 3, 1, 1, 4]
        
        Step 0: 
        l, r = 0, 0 
        
        is goal in range? - No, add jumps
        
        then we can jump by 2
        
        Step 1: 
        l = 1, r = 2
        
        is goal in range? - No, add jumps
        
        then we can jump by max(nums[l], nums[r])
        
        Step 2: 
        l = 3, r = 4
        
        is goal in range? - Yes, return jumps
        """

        print(f"l: {l}, r: {r}, max_jump: {max(nums[l:r + 1])} processing range: {nums[l:r+1]}")
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = min(max(farthest, i + nums[i]), len(nums))
            l = r + 1
            r = farthest
            jumps += 1
            print(f"l: {l}, r: {r}, max_jump: {max(nums[l:r + 1])} processing range: {nums[l:r + 1]}")

        return jumps
