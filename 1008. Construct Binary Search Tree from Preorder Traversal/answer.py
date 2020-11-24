class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(root, node):
    if root is None:
        root = TreeNode(node)

    elif root.val > node:
        if root.left is None:
            root.left = TreeNode(node)
        else:
            build_tree(root.left, node)

    elif root.val < node:
        if root.right is None:
            root.right = TreeNode(node)
        else:
            build_tree(root.right, node)

    return root

    root = None
    for node in preorder:
        root = build_tree(root, node)

    return root
