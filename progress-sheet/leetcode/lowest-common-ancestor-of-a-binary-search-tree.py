# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,path):
            nonlocal p_path, q_path
            if not root:
                return
            path.append(root)
            if root.val == q.val:
                q_path = path.copy()
            if root.val == p.val:
                p_path = path.copy()
            dfs(root.left,path.copy())
            dfs(root.right,path.copy())

        p_path = []
        q_path = []
        dfs(root, [])
        for i in range(min(len(p_path), len(q_path))):
            print(p_path[i].val,q_path[i].val)
            if p_path[i].val != q_path[i].val:

                return p_path[i-1]

        return p_path[min(len(p_path), len(q_path))-1]  


             
            