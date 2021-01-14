"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node, max_depth):
            if not node:
                return 0
            arr = [0]
            for child in node.children:
                arr.append(dfs(child, max_depth))

            return 1 + max(arr)

        return dfs(root, 0)
