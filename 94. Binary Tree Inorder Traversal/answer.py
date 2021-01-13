def inorderTraversal(self, root):
    res = []

    def inorder(root, res):
        if not root:
            return

        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)

    inorder(root, res)
    return res