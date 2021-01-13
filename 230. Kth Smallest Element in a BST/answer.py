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

        def dfs(node):
            if not node:
                return
            val = node.val
            values.append(val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(values)
        return sorted(values)[k-1]
