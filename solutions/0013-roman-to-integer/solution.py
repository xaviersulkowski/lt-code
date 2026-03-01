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

        result = 0 

        for i in range(0, len(s) - 1, 1): 
            c1 = romanMap[s[i]]
            c2 = romanMap[s[i+1]]

            if c2 > c1: 
                result -= c1
            else: 
                result += c1 

        result += romanMap[s[-1]]

        return result

            


        
