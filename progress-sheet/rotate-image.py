class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        n = len(matrix)
        m  = len(matrix[0])
        setter = set()
        for i in range(n):
            for j in range(m):
                if (j,i) not in setter:
                    matrix[i][j], matrix[j][i] = matrix[j][i] , matrix[i][j]
                    setter.add((i,j))

        for row in matrix:
            row.reverse()