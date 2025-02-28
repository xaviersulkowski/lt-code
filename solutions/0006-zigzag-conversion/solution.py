class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1: 
            return s

        rows = [''] * min(numRows, len(s))
        
        row, desc = 0, False

        for c in s: 
            rows[row] += c
            if row == 0 or row == numRows - 1: 
                desc = not desc 
            row += 1 if desc else -1 

        return ''.join(rows)

