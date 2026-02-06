class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): 
            return False 

        l, p = 0, 0
        while p < len(t) and l < len(s): 
            if s[l] == t[p]:
                l += 1
            p += 1 
        
        return True if l == len(s) else False
            
