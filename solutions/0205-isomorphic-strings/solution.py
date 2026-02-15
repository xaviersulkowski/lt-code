class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s, map_t = {}, {}
        
        for x, y in zip(s, t): 
            if (
                (x in map_s and map_s[x] != y) or 
                (y in map_t and map_t[y] != x)
            ):
                return False
            
            map_s[x] = y
            map_t[y] = x

        return True

