class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for x in range(9)]
        columns = [set() for x in range(9)]
        grids = [set() for x in range(9)] # 0, 1, 2
                                          # 3, 4, 5, 
                                          # 6, 7, 8 

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                grid_index = (r // 3) * 3 + (c // 3)
                
                if val == ".":
                    continue 

                row = rows[r]
                if val in row: 
                    return False
                else:
                    rows[r].add(val)
                
                column = columns[c]
                if val in column: 
                    return False
                else:
                    columns[c].add(val)
                
                grid = grids[grid_index]
                if val in grid:
                    return False
                else: 
                    grids[grid_index].add(val)

        return True
                
            


                

