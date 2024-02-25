# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root,pos):
            nonlocal hmap
            if not root:
                return
            hmap[pos[1]].append((pos[0], root.val))
            row, col = pos
            dfs(root.left,[row +1 , col -1])
            dfs(root.right, [row+1, col+1])
        
        hmap = defaultdict(list)
        dfs(root,(0,0))
        
        hmap = dict(sorted(hmap.items(), key = lambda x : x[0]))
        for cols in hmap.values():
            cols.sort()
            for j in range(len(cols)):
                cols[j] = cols[j][1]

        return list(hmap.values())

        