class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        open_brackets = list(bracket_pairs.values())
        closing_brackets = list(bracket_pairs.keys())
        
        stack = []

        for c in s: 
            if c in open_brackets: 
                stack.append(c) 
            else: 
                if len(stack) > 0 and bracket_pairs[c] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True 
        return False


        

