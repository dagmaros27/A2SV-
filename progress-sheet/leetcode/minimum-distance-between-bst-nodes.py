# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return []
            s = [root.val]
            l = dfs(root.left)
            r = dfs(root.right)
            return l + s + r
        stk = dfs(root)
        mnm = float('inf')
        for i in range(len(stk)):
            for j in range(i+1,len(stk)):
                mnm = min(mnm,stk[j] - stk[i])
            

        return mnm

            




        