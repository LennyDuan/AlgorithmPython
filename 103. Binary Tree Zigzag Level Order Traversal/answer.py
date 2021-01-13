# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root:
            return []
        queue = [root]
        order = True

        while queue:
            next_level = []
            curr_list = []
            for ele in queue:
                if ele.left:
                    next_level.append(ele.left)
                if ele.right:
                    next_level.append(ele.right)

            if order:
                for ele in queue:
                    curr_list.append(ele.val)
                order = False
            else:
                for ele in reversed(queue):
                    curr_list.append(ele.val)
                order = True

            queue = next_level
            res.append(curr_list)
        return res


