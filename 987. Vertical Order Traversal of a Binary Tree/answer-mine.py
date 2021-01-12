from collections import defaultdict


def verticalTraversal(self, root):
    res = []
    pre_res = defaultdict(list)
    x = y = 0

    def construct_res(node, x, y, pre_res):
        pre_res[x].append((node.val, y))
        if node.left:
            construct_res(node.left, x - 1, y - 1, pre_res)
        if node.right:
            construct_res(node.right, x + 1, y + 1, pre_res)

    construct_res(root, x, y, pre_res)

    sorted_pre = dict(sorted(pre_res.items()))
    for items in sorted_pre.values():
        res.append([i for i, j in sorted(items, key=lambda x: x[1])])
    return res


verticalTraversal(None, None)
