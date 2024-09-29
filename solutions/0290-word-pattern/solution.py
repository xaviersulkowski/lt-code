class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split(' ')):
            return False 

        patternMap = {}

        for i, j in zip(pattern, s.split(' ')):
            if patternMap.get(i) is None: 
                if j not in patternMap.values():
                    patternMap[i] = j 
                else: 
                    return False
            
            if patternMap.get(i) is not None and patternMap[i] != j: 
                return False
        
        return True

