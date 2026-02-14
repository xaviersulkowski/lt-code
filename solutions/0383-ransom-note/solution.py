class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazineCounts = {}
        for x in magazine: 
            magazineCounts[x] = 1 + magazineCounts.get(x, 0)
        
        for c in ransomNote:
            if c in magazineCounts and magazineCounts[c] > 0:
                magazineCounts[c] -= 1 
            else: 
                return False

        return True 
