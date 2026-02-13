class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        col = len(matrix[0])

        transpose = [[None]*rows for _ in range(col)]
        print(transpose)

        for i in range(col):
            for j in range(rows):
                transpose[i][j] = matrix[j][i]
        
        return transpose