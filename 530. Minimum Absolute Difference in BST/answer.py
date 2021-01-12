def getMinimumDifference(self, root: TreeNode) -> int:
    res = [float('inf')]
    pre = [float('-inf')]

    def inorder(node):
        if not node:
            return

        inorder(node.left)
        res[0] = min(res[0], abs(node.val - pre[0]))
        pre[0] = node.val
        inorder(node.right)

    inorder(root)
    return res[0]
