# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def widthOfBinaryTree(root: TreeNode) -> int:
    wight = 0
    queue = [(1, root)]

    while queue:
        wight = max(wight, queue[-1][0] - queue[0][0] + 1)
        next_queue = []
        for obj in queue:
            num, item = obj
            if item.left:
                next_queue.append((num * 2, item.left))
            if item.right:
                next_queue.append(((num * 2 + 1), item.right))
        queue = next_queue
    return wight


class Solution:
    pass