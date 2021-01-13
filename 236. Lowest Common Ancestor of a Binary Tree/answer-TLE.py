# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find_ele(node, check_node):
            if not node:
                return

            if node.val == check_node.val:
                return True

            return find_ele(node.left, check_node) or find_ele(node.right, check_node)

        res = [root]

        def dfs(node, res):
            if not node:
                return

            if find_ele(node, p) and find_ele(node, q):
                res[0] = node
                dfs(node.left, res)
                dfs(node.right, res)

            else:
                return
        dfs(root, res)
        return res[0]