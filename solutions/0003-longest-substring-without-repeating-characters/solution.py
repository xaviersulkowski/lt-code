class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest = 0, 0
        charset = set()

        for r in range(len(s)): 
            while s[r] in charset: 
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            longest = max(longest, len(charset))

        return longest
                    

