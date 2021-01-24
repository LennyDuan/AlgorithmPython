# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def travesal(o, c):
            if o:
                if o is target:
                    return c
                return travesal(o.left, c.left) or travesal(o.right, c.right)

        return travesal(original, cloned)
