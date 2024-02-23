# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # maxLeft = 0
        # minRight = float('inf')
        # def validate(root):
        #     if not root:
        #         return
        #     if not root.left and not root.right:
        #         return True
        #     if root.left and root.val <= root.left.val:
        #         return False
        #     if root.right and root.val >= root.right.val:
        #         return False
            
        #     return validate(root.left) and validate(root.right) 
        # return validate(root)

        def traverse(root):
            if not root:
                return []
            s = [root.val]
            l = traverse(root.left)
            r = traverse(root.right)
            return l + s + r
        stk = traverse(root)

        for i in range(len(stk)-1):
            if stk[i] >= stk[i+1]:
                return False
        return True
       
        
            

            
            
        