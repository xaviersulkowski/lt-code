class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for rn in ransomNote: 
            if rn not in magazine:
                return False 
            
            magazine = magazine.replace(rn, '', 1)

        return True
