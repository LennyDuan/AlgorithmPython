def rotateRight(self, head, k: int):
    if not head:
        return head
    def rotate(head):
        last = None
        pre_last = None
        tmp = node = head
        l = 0
        while node:
            l += 1
            if node.next:
                pre_last = node
                last = node.next
                node = node.next

            else:
                if pre_last:
                    pre_last.next = None
                    last.next = tmp
                    return l, last
                return l, tmp

    while k > 0:
        l, head = rotate(head)
        k -= 1
        k = k % l

    return head
