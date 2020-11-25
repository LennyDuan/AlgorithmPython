def isBalanced(self, root: TreeNode) -> bool:


    def check(node):
        if node is None:
            return 0, True

        l_d, l_b = check(node.left)
        r_d, r_b = check(node.right)

        node_d = max(l_d, r_d) + 1
        node_b = l_b and r_b and abs(l_d - r_d) <= 1

        return node_d, node_b

    def check2(node):



    return check(root)[1]



