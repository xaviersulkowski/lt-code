class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])

        first_row_zeros = False 

        for i in range(h): 
            for j in range(w): 
                if matrix[i][j] == 0:
                    matrix[0][j] = 0

                    if i > 0: 
                        matrix[i][0] = 0
                    else:
                        first_row_zeros = True 

        for i in range(1, h):
            for j in range(1, w):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0: 
            for i in range(h): 
                matrix[i][0] = 0
            
        if first_row_zeros is True: 
            for j in range(w): 
                matrix[0][j] = 0
            
                
