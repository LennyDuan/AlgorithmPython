# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    def merge(root1, root2):
        if root1 and root2:
            root1.val = root1.val + root2.val
            root1.left = merge(root1.left, root2.left)
            root1.right = merge(root1.right, root2.right)
            return root1
        else:
            return root1 or root2

    merged = merge(t1, t2)

    return merged


def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not (t1 and t2):
        return t1 or t2

    q1 = [t1]
    q2 = [t2]

    while q1 and q2:
        q1n = q1.pop(0)
        q2n = q2.pop(0)

        if q1n and q2n:
            q1n.val = q1n.val + q2n.val
            if (not q1n.left) and q2n.left:
                q1n.left = TreeNode(0)
            if (not q1n.right) and q2n.right:
                q1n.right = TreeNode(0)
            q1.append(q1n.left)
            q1.append(q1n.right)
            q2.append(q2n.left)
            q2.append(q2n.right)

    return t1
