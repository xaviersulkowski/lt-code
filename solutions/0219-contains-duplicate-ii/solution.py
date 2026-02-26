class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() 
        l = 0 
        for r in range(len(nums)): 
            n = nums[r]
            if r - l > k: 
                window.remove(nums[l])
                l +=1 

            if n in window: 
                return True 
            
            window.add(n)
            
        return False

