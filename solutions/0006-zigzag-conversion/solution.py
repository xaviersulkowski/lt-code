class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: 
            return s 
        
        # approach 1: 

        # res = ""
        # step = 2 * (numRows - 1)
        # for i in range(numRows): 
        #     for j in range(i, len(s), step):
        #         res += s[j] 
        #         if i > 0 and i < numRows - 1 and (j + step - 2 * i) < len(s):
        #             res += s[j + step - 2 * i] 

        # return res

        # approach 2: 

        res = [""] * numRows 
        row = 0 
        go_down = False
        for ch in s: 
            res[row] += ch 
            
            if row == 0 or row == numRows - 1: 
                go_down = not go_down
            
            row = row + 1 if go_down else row - 1
        
        return "".join(res)

