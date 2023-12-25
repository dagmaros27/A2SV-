class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum = 0
        n = len(mat)
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i-j == 0:
                    sum += mat[i][j]
                elif j+i == n-1:
                    sum += mat[i][j]  
        
        return sum