class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0 

        for i in range(len(s) - 1): 
            num1 = symbols[s[i]]
            num2 = symbols[s[i + 1]]
            
            if num2 > num1:
                res -= num1
            else: 
                res += num1 
        
        res += symbols[s[-1]]
        return res 
            

