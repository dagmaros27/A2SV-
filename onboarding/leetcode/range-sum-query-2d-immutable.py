class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.pf = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i== 0 and j == 0:
                    self.pf[i][j] = matrix[i][j]
                elif i == 0:
                    self.pf[i][j] = self.pf[i][j-1] + matrix[i][j]
                elif j == 0:
                    self.pf[i][j] = self.pf[i-1][j] + matrix[i][j]
                else:
                    self.pf[i][j] = self.pf[i-1][j] + self.pf[i][j-1] - self.pf[i-1][j-1] + matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = 0 if row1 == 0 else self.pf[row1-1][col2]
        left = 0 if col1 == 0 else self.pf[row2][col1-1]
        diagonal = 0 if row1 == 0 or col1 == 0 else self.pf[row1-1][col1-1]

        return self.pf[row2][col2] - left - top + diagonal

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)