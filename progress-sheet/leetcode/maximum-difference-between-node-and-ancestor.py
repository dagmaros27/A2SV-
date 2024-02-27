# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(root,path):
            nonlocal mxm
            if not root:
                return 
            if path:
                for i in path:
                    mxm = max(mxm,abs(root.val - i))
            path.append(root.val)


            if root.left:
                dfs(root.left, path.copy())

            if root.right:
                dfs(root.right, path)

        mxm = 0
        dfs(root,[])
        return mxm
            

        