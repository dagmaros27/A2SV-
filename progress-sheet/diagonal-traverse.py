from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n = len(mat)
        m = len(mat[0])
        up_flag = True

        i, j = 0, 0

        while i < n and j < m:

            while up_flag:
                if (0 <= i < n and 0 <= j < m):
                    ans.append(mat[i][j])
                    i -= 1
                    j += 1
                if not (0 <= i < n and 0 <= j < m):
                    up_flag = False

                    if i < 0 and j < m:
                        i = 0
                    elif j == m:
                        i += 2
                        j -= 1

            while not up_flag:
                
                if (0 <= i < n and 0 <= j < m):
                    ans.append(mat[i][j])
                    i += 1
                    j -= 1

                if not (0 <= i < n and 0 <= j < m):
                    up_flag = True
                    if j < 0 and i < n:
                        j = 0
                    elif i == n:
                        j += 2
                        i -= 1

        return ans
