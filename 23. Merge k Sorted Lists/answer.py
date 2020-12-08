# mergeKList by heap
import heapq


def mergeKLists(self, lists):
    q = [(l.val, index) for index, l in enumerate(lists) if l]
    heapq.heapify(q)
    head = cur = ListNode()
    while q:
        c_v, c_i = heapq.heappop(q)
        cur.next = ListNode(c_v)
        cur = cur.next
        lists[c_i] = lists[c_i].next
        if lists[c_i]:
            heapq.heappush(q, (lists[c_i].val, c_i))

    return head.next


# mergeKList one by one
def mergeKLists(self, lists):
    def merge_two_lists(l1, l2):
        head = cur = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return head.next

    if len(lists) == 0:
        return ListNode().next

    while len(lists) > 1:
        l1 = lists.pop(0)
        l2 = lists.pop(0)
        new = merge_two_lists(l1, l2)
        lists.append(new)

    return lists[0]
