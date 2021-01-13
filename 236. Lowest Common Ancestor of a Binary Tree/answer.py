# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursive(node):
            if not node:
                return
            left = recursive(node.left)
            right = recursive(node.right)
            mid = node.val == p.val or node.val == q.val

            if left + mid + right >= 2:
                self.res = node
            return left or mid or right
        recursive(root)

        return self.res
