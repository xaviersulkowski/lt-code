class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(needle) > len(haystack)) or needle == "":
            return -1

        for i in range(0, len(haystack) + 1 - len(needle)):
            if haystack[i] == needle[0] and needle == haystack[i:i+len(needle)]:
                return i

        return -1
