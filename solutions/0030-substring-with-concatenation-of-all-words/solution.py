class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        counts = {}
        res = []

        for w in words: 
            counts[w] = 1 + counts.get(w, 0)
        
        for i in range(len(words[0])):
            start = i 
            window = {}
            have = 0 

            for l in range(i, len(s) - n + 1, n):
                word = s[l:l+n]
                window[word] = 1 + window.get(word, 0)

                if word in counts: 
                    have += 1 

                    while window[word] > counts[word]:
                        left_str = s[start:start+n]
                        window[left_str] -= 1 
                        start += n 
                        have -= 1 

                    if have == len(words):
                        res.append(start)

                else:
                    have = 0 
                    window = {}
                    start = l + n

        return res
