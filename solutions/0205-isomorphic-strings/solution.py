class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        map_s = {}
        map_t = {}

        for i, j in zip(s, t): 
            if ((i in map_s and map_s[i] != j) or (j in map_t and map_t[j] != i)):
                return False
            map_s[i] = j 
            map_t[j] = i
        
        return True
