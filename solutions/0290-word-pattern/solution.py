class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        map_pattern = {}
        map_s = {}

        s = s.split()

        if len(s) != len(pattern): 
            return False

        for p, c in zip(pattern, s): 
            if (p in map_pattern and map_pattern[p] != c) or ((c in map_s and map_s[c] != p)): 
                return False 
            
            map_pattern[p] = c
            map_s[c] = p

        return True
