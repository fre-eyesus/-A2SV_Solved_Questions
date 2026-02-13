class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        col,row = len(matrix),len(matrix[0])

        for i in range(row):
            for j in range(i+1, col):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for r in range(row):
            matrix[r].reverse()



