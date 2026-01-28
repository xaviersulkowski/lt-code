class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for i in s[::-1]:
            if i == " " and length > 0:
                return length
            if i != " ":
                length += 1

        return length
