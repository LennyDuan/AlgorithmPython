def minDiffInBST(self, root: TreeNode) -> int:
    res = [float('inf')]
    pre = [float('-inf')]

    def inorder(node, res, pre):
        if not node:
            return

        inorder(node.left, res, pre)
        res[0] = min(res[0], node.val - pre[0])
        pre[0] = node.val
        inorder(node.right, res, pre)

    inorder(root, res, pre)

    return res[0]
