def sortedListToBST(self, head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    def list_to_bst(l,r):
        if l > r:
            return
        mid = (r + l) // 2
        node = TreeNode(values[mid])
        if l == r:
            return node

        node.left = list_to_bst(l, mid - 1)
        node.right = list_to_bst(mid + 1, r)
        return node

    return list_to_bst(0, len(values) - 1)
