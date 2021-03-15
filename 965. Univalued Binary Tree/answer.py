def isUnivalTree(self, root) -> bool:
    if not root:
        return True
    res = [root.val, True]

    def dfs(node):
        if not node or not res[1]:
            return
        if node.val is not res[0]:
            res[1] = False
            return
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res[1]