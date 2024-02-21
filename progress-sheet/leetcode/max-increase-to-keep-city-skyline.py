class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mxm_row = []
        mxm_col = []
        for i in range(n):
            mxm = 0
            for j in range(n):
                mxm = max(mxm, grid[j][i])
            mxm_col.append(mxm)
        for i in grid:
            mxm_row.append(max(i))
        ans = 0
        
        
        for i in range(n):
            for j in range(n):
                ans += min(mxm_row[i], mxm_col[j]) - grid[i][j] 
        return ans
                

