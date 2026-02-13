class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or s == "":
            return ""
        
        window, counts = {}, {}

        for x in t: 
            counts[x] = 1 + counts.get(x, 0)
        
        need, have = len(counts), 0

        res, res_len = (-1, -1), float('inf')

        l = 0 
        for r in range(len(s)): 
            c = s[r]
            
            window[c] = 1 + window.get(c, 0)
            
            if c in counts and window[c] == counts[c]: 
                have += 1
            
            while need == have: 
               
                window[s[l]] -= 1

                if (r - l + 1) < res_len: 
                    res_len = (r - l + 1)
                    res = (l, r)

                if s[l] in counts and window[s[l]] < counts[s[l]]:
                    have -= 1 

                l += 1
        
        return s[res[0]:res[1]+1]
