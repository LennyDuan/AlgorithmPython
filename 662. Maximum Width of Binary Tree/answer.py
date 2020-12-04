def widthOfBinaryTree(self, root) -> int:
    max_row = 0
    # tree_queue = [root]
    # tree_arr_bfs = [root.val]
    #
    # while tree_queue:
    #     node = tree_queue.pop(0)
    #
    #     if node.left:
    #         tree_arr_bfs.append(node.left.val)
    #         tree_queue.append(node.left)
    #     else:
    #         tree_arr_bfs.append(0)
    #
    #     if node.right:
    #         tree_arr_bfs.append(node.right.val)
    #         tree_queue.append(node.right)
    #     else:
    #         tree_arr_bfs.append(0)

    tree_arr_bfs = [1, 3, 2, 5, 3, 0, 9, 0, 0, 0, 0, 0, 0]
    #[1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]

    two_level = 0
    index = 0
    bfs_len = len(tree_arr_bfs)

    print(tree_arr_bfs)

    while index < bfs_len:
        current_level_range = 2 ** two_level

        right_index = index + current_level_range
        right_i = right_index if right_index < bfs_len else bfs_len - 1
        print('{}: {} - > {}'.format(current_level_range, index, right_i))
        while not tree_arr_bfs[right_i - 1] and right_i > index:
            right_i -= 1

        max_row = max(max_row, right_i - index)

        two_level += 1
        index = right_index

    print(max_row)
    return max_row


widthOfBinaryTree(None,
                  {'val': 1}
                  )
