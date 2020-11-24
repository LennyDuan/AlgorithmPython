class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)

    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)

    else:
        return root



def lowestCommonAncestor(root, p, q):
    node = root
    while node:

        if node.val > p.val and node.val > q.val:
            node = node.left

        if node.val < p.val and node.val < q.val:
            node = root.right

    return node
