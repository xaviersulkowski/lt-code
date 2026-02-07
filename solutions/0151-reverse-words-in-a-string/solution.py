class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) - 1
        res = []
        while i >= 0: 
            if s[i] != " ":
                j = i 
                while j >= 0 and s[j] != " ": 
                    j -= 1

                res.append(s[j+1:i+1])
                i = j
            i -= 1
        
        return " ".join(res)
