class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        l, r = 0, n - 1

        while l < r: 
            t, b = l, r 

            for i in range(r - l): 
                
                top_left = matrix[t][l + i]

                # replace top left with bottom left
                matrix[t][l + i] = matrix[b - i][l]

                # replace bottom left with bottom right
                matrix[b - i][l] = matrix[b][r - i]

                # replace bottom right with top right
                matrix[b][r - i] = matrix[t + i][r]

                # replace top right with bottom left
                matrix[t + i][r] = top_left

            l += 1 
            r -= 1
