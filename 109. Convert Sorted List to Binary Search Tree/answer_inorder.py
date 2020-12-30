def sortedListToBST(self, head):
    values = []
    tmp = head
    while tmp:
        values.append(tmp.val)
        tmp = tmp.next

    def inorder(l, r):
        nonlocal head

        if l > r:
            return

        mid = (r + l) // 2

        left = inorder(l, mid - 1)

        node = TreeNode(head.val)

        head = head.next
        node.left = left
        node.right = inorder(mid + 1, r)
        return node

    return inorder(0, len(values) - 1)
