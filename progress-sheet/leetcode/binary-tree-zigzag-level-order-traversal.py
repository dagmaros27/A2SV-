# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hmap = defaultdict(list)

        def dfs(root,row):
            if not root:
                return 
            hmap[row].append(root.val)
            dfs(root.left,row+1)
            dfs(root.right,row+1)
        dfs(root,0)
        ans = []
        for i in hmap:
            curr = []
            if i%2 == 0:
                for j in hmap[i]:
                    curr.append(j)
            else:
                for j in reversed(hmap[i]):
                    curr.append(j)
            ans.append(curr)




        return ans 


        

        
