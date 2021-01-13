# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_val = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def find_max(node):
            if not node:
                return 0

            left_max = max(0, find_max(node.left))
            right_max = max(0, find_max(node.right))

            self.max_val = max(self.max_val, left_max + right_max + node.val)
            return max(left_max, right_max) + node.val

        find_max(root)

        return self.max_val
