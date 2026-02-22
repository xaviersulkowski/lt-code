class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r: 
            val_l = numbers[l]
            val_r = numbers[r]

            if val_l + val_r == target: 
                return [l + 1, r + 1]
            
            if val_l + val_r > target: 
                r -= 1 
            
            if val_l + val_r < target: 
                l += 1 
