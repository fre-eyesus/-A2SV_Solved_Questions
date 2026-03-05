class NumMatrix:

    def __init__(self, matrix):
     
        n = len(matrix)
        m = len(matrix[0])

        self.pre = [[0] * (m + 1) for _ in range(n + 1)]

        for r in range(n):
            pref = 0
            for c in range(m):
                pref += matrix[r][c]
                above = self.pre[r][c+1]

                self.pre[r+1][c+1] = pref + above

               
    def sumRegion(self, row1, col1, row2, col2):
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1

        bottomR = self.pre[row2][col2]
        above = self.pre[row1-1][col2]
        left = self.pre[row2][col1-1]
        topLeft = self.pre[row1-1][col1-1]

        return bottomR - above - left + topLeft

        