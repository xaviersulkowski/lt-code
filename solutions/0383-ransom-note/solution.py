class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCounts = {}

        for s in magazine: 
            magazineCounts[s] = magazineCounts.get(s, 0) + 1 

        for c in ransomNote: 
            if c in magazineCounts and magazineCounts[c] > 0: 
                magazineCounts[c] -= 1
            else: 
                return False

        return True 
