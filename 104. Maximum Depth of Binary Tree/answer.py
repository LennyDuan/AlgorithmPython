# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max = 0
        def dfs(node, max):
            if not node:
                return 0
            left_max = dfs(node.left, max)
            right_max = dfs(node.right, max)
            return 1 + max(left_max, right_max)

        return dfs(root, max)