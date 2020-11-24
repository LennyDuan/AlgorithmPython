class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root, val):
    head = root

    def build_tree(root, head, val):
        if root is None:
            return TreeNode(val)

        if root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
                return head
            else:
                return build_tree(root.left, head, val)
        if root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
                return head
            else:
                return build_tree(root.right, head, val)

    return build_tree(root, head, val)
