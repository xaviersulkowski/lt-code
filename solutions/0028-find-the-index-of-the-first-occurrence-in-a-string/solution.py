class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # import re 

        # out = re.search(f"{needle}", haystack)
        # if not out: 
        #     return -1 
        # else: 
        #     return out.start()

        needle_len = len(needle)

        for i in range(len(haystack) - needle_len + 1):
            if haystack[i : i + needle_len] == needle: 
                return i
        return -1 

