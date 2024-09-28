class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        prev_index = -1

        for i in s: 
            idx = t.find(i, prev_index + 1)
            
            if idx == -1:
                return False
            
            prev_index = idx
        
        return True 
