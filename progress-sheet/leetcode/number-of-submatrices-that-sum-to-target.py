class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
    
        count = 0
        for i in range(n):
            for j in range(i, n):
                map = {}
                map[0] = 1
                sum = 0
                for k in range(m):
                    sum += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    count += map.get(sum - target, 0)
                    map[sum] = map.get(sum, 0) + 1
    
        return count