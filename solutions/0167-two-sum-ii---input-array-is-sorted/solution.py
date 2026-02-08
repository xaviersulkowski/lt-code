class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r: 
            numl = numbers[l]
            numr = numbers[r]

            if numl + numr == target: 
                return [l + 1, r + 1]
            
            if numr + numl > target: 
                r -= 1 

            if numr + numl < target: 
                l += 1

