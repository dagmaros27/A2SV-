# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
    def maxSumBST(self, root:TreeNode) -> int:
     def dfs(node):
        nonlocal max_sum

        if not node:
            return 0, float('inf'), float('-inf')

        left_sum, left_min, left_max = dfs(node.left)
        right_sum, right_min, right_max = dfs(node.right)

        if left_max < node.val < right_min:
            current_sum = left_sum + right_sum + node.val
            max_sum = max(max_sum, current_sum)
            return current_sum, min(left_min, node.val), max(right_max, node.val)
        else:
            return float('-inf'), 0, 0

     max_sum = 0
     dfs(root)
     return max_sum