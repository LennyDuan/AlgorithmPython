def rightSideView(self, root):

    if not root:
        return root

    res = []
    queue = [(root, 1)]
    res_list = [(root.val, 1)]

    while queue:
        val = queue.pop(0)
        c_node, level = val[0], val[1]

        if c_node and c_node.right:
            res_list.append((c_node.right.val, level + 1))
            queue.append((c_node.right, level + 1))

        if c_node and c_node.left:
            res_list.append((c_node.left.val, level + 1))
            queue.append((c_node.left, level + 1))

    print(res_list)

    level = 1
    for node in res_list:
        val, lev = node[0], node[1]

        if level == lev:
            res.append(val)
            level += 1
    print(res)
    return res
