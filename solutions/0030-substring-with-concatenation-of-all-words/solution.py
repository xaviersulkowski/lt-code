class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        counts = {}
        res = []
        l = 0

        for w in words: 
            counts[w] = 1 + counts.get(w, 0)


        for i in range(n):
            start = i
            window = {}
            have = 0
        
            for l in range(i, len(s) - n + 1, n):    
                sub = s[l:l+n]

                if sub in counts: 
                    have += 1 
                    window[sub] = 1 + window.get(sub, 0)

                    while window[sub] > counts[sub]:
                        window[s[start:start + n]] -= 1
                        start += n
                        have -= 1
                    
                    if have == len(words):
                        res.append(start)

                else:
                    start = l + n
                    window = {}
                    have = 0

        return res
                
                    
                
