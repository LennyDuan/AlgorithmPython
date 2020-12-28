from collections import defaultdict


def levelOrder(self, root: TreeNode):
    queue = [(0, root)]
    d = defaultdict(list)
    while queue:
        c_q = queue.pop(0)
        row, node = c_q
        if node:
            d.get(row, []).append(node.val)
            if node.left:
                queue.append((row + 1, node.left))
            if node.right:
                queue.append((row + 1, node.right))

    return list(d.values())
