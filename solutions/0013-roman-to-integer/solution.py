class Solution:
    def romanToInt(self, s: str) -> int:

        romanMap = {
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        finalInt = 0

        latestInt = None

        for r in reversed(s): 
            i = romanMap[r]
            
            if latestInt is None:
                latestInt = i 
            
            if i < latestInt: 
                finalInt -= i 
            else: 
                finalInt += i 
            
            latestInt = i
    
        return finalInt

            


        
