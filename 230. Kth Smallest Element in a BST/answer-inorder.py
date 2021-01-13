# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            val = node.val
            values.append(val)
            inorder(node.right)
            
        inorder(root)
        return values[k-1]
