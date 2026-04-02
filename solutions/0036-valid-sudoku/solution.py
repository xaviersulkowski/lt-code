class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _  in range(9)]
        columns = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9): 
                element = board[r][c]

                if element == ".": 
                    continue 

                g_key = (r // 3) * 3 + (c // 3)

                if element in rows[r]: 
                    return False

                if element in columns[c]: 
                    return False

                if element in grids[g_key]: 
                    return False

                rows[r].add(element)
                columns[c].add(element)
                grids[g_key].add(element)

        return True
