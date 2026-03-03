class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        n = len(matrix)
        m = len(matrix[0])

        self.pre = [[0 for i in range(m+1)] for j in  range(n+1)]

        for i in range(n):
            for j in range(m):
                self.pre[i][j] = matrix[i][j] + self.pre[i - 1][j] + self.pre[i][j-1] - self.pre[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        box = self.pre[row2][col2]
        l_box = self.pre[row2][col1-1]
        u_box = self.pre[row1-1][col2]

        overlap = self.pre[row1-1][col1-1]

        return box - l_box - u_box + overlap


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)