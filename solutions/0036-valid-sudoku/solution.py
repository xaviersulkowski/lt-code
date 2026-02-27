class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for x in range(9)]
        columns = [set() for x in range(9)]
        groups = [set() for x in range(9)]

        for i in range(9):
            for j in range(9): 
                
                num = board[i][j]

                if num == ".": 
                    continue 

                if num in rows[i]:
                    return False
                
                if num in columns[j]:
                    return False 

                group_key = (i // 3) * 3 + (j // 3)
                if num in groups[group_key]:
                    return False

                rows[i].add(num)
                columns[j].add(num)
                groups[group_key].add(num)
        
        return True
