class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        rBrackets = {
            v: k for k, v in brackets.items()
        }

        stack = []

        for c in s: 
            if c in brackets.keys():
                stack.append(c)
            else: 
                if len(stack) > 0 and stack[-1] == rBrackets[c]: 
                    stack.pop(-1)
                else:
                    return False

        return True if len(stack) == 0 else False
