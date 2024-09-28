class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        letters_map = {}

        for a, b in zip(s, t): 
            
            if letters_map.get(a) is None:
                if b in letters_map.values(): 
                    return False
                else:
                    letters_map[a] = b 
            elif letters_map[a] == b:
                pass 
            else: 
                return False 
        
        return True
