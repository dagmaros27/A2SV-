# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return []
            s = [root.val]
            l = dfs(root.left)
            r = dfs(root.right)

            return l+s+r
        
        ans = dfs(root)
        counter = Counter(ans)
        mxm = max(counter.values())
        res = []
        for i in counter:
            if counter[i] == mxm:
                res.append(i)
        return res
        