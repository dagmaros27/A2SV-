class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        max_sum = 0
        for i in range(n):
            for j in range(m):
                if i+2 < n and j+2 < m:
                    max_sum = max(max_sum, self.hourglass_sum(grid,i,j))
        
        return max_sum
        
        

    def hourglass_sum(self,matrix,i,j):
        sum = 0
        x = j
        while x < j +3:
            sum += matrix[i][x] + matrix[i+2][x]
            x += 1
        
        sum += matrix[i+1][j+1]

        return sum

            
        