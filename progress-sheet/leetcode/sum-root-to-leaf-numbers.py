# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,path):
            nonlocal ans
            if not root:
                return
            path.append(str(root.val))
            if not root.right and not root.left:
                ans += int("".join(path))
            if root.left:
                dfs(root.left,path.copy())
            if root.right:
                dfs(root.right,path)
        ans = 0
        dfs(root,[])
        return ans

        