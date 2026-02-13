class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = len(matrix[0])
        rows = len(matrix)

        mark_col = [0]*cols
        mark_row  = [0]*rows

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    mark_row[i] = 1
                    mark_col[j] = 1
        for i in range(rows):
            for j in range(cols):
                if mark_row[i] == 1 or mark_col[j] == 1:
                    matrix[i][j] = 0
        






        