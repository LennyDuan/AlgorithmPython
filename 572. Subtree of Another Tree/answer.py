# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def is_sub(s_node, t_node):
            if not s_node and not t_node:
                return True

            if s_node and t_node:
                if s_node.val != t_node.val:
                    return False
                else:
                    return is_sub(s_node.left, t_node.left) and is_sub(s_node.right, t_node.right)
            return False

        res = [False]

        def dfs(s, t):
            if not s or not t:
                return
            if s.val == t.val:
                if is_sub(s, t):
                    res[0] = True
            dfs(s.left, t)
            dfs(s.right, t)
        dfs(s, t)
        return res[0]


