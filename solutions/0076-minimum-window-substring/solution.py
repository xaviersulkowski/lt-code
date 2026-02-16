class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts, window = {}, {}
        for x in t: 
            counts[x] = 1 + counts.get(x, 0)
        
        need, have = len(counts), 0

        res, res_len = (), float('inf')

        l = 0 
        for r in range(len(s)): 
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in counts and window[c] == counts[c]: 
                have += 1

            while need == have: 
                c2 = s[l]

                window[c2] -= 1 

                if c2 in counts and window[c2] < counts[c2]:
                    have -= 1 
                
                if r - l + 1 < res_len:
                    res_len = r - l + 1 
                    res = (l, r)
                
                l += 1 

        return "" if res_len == float('inf') else s[res[0]:res[1]+1]
