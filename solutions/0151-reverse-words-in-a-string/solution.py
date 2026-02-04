class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        j, i = n - 1, n - 1
        out = []
        while i >= 0: 
            if s[i] == " ": 
                i -= 1 
            else: 
                j = i 
                while i >= 0 and s[i] != " ":
                    i -= 1
                out.append(s[i+1:j+1])
                
        
        return " ".join(out)
