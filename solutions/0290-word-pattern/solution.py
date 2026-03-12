class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_p = {}
        map_s = {} 

        s = s.split(" ")
        if len(s) != len(pattern):
            return False

        for p, c in zip(pattern, s): 
            if (
                (p in map_p and map_p[p] != c ) 
                or (c in map_s and map_s[c] != p)
            ): 
                return False
            map_p[p] = c
            map_s[c] = p

        return True 
