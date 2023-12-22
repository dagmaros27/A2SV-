class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        for i in range(n):
            col_bool =  self.validColumn(i,board)
            row_bool = self.validRow(i,board)
            if not (col_bool and row_bool):
                return False
        
        for i in range(0,n,3):
            for j in range(0,n,3):
                box_bool = self.validBox(i,j,board)
                if not box_bool:
                    return False
        
        return True


    def validColumn(self,j, matrix ):
        unique = set()
        for i in range(9):
            if matrix[i][j] in unique and matrix[i][j] != ".":
                return False
            unique.add(matrix[i][j])
        return True

    def validRow(self,i,matrix):
        unique = set()
        for j in range(9):
            if matrix[i][j] in unique and matrix[i][j] != ".":
                return False
            unique.add(matrix[i][j])
        return True

    def validBox(self, i, j, matrix):
        unique = set()
        for k in range(3):
            for l in range(3):
                if matrix[i+k][j+l] in unique and matrix[i+k][j+l] != ".":
                    print(unique)
                    return False
                unique.add( matrix[i+k][j+l])     
        return True
        