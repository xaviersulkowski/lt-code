class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: 
            return s 
        
        # Approach 1: step 
        # res = ""
        # step = 2 * (numRows - 1)
        
        # for r in range(numRows): 
        #     for i in range(r, len(s), step):
        #         res += s[i]
        #         if r > 0 and r < numRows -1 and (i + step - 2 * r ) < len(s): 
        #             res += s[i + step - 2 * r ]
        
        # return res

        # Approach 2: fill in rows 
        res = [""] * numRows
        going_down = True
        row = 0
        for ch in s: 
            res[row] += ch
            
            if row == 0: 
                going_down = True 
            elif row == numRows - 1: 
                going_down = False 
            
            if going_down: 
                row += 1 
            else: 
                row -= 1
        
        return "".join(res)
