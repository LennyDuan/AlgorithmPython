def levelOrder(self, root: TreeNode):
    res = []
    level = [root]

    while level and root:
        current_list = []
        next_level = []

        for node in level:
            if node:
                current_list.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        level = next_level
        res.append(current_list)
    return res
