def isValidBST(self, root):
    def check_tree(node, low, high):
        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return check_tree(node.left, low, node.val) and check_tree(node.right, node.val, high)

    return check_tree(root, float('-inf'), float('inf'))
