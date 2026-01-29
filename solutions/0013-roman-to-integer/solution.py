class Solution:
    def romanToInt(self, s: str) -> int:
        roman_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        i = 0
        while i < len(s) - 1:
            if roman_integer[s[i]] < roman_integer[s[i + 1]]:
                res -= roman_integer[s[i]]
            else:
                res += roman_integer[s[i]]
            i += 1

        res += roman_integer[s[-1]]

        return res

