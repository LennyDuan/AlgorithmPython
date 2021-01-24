# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def find_mid(head):
            slow = ListNode()
            while head and head.next:
                slow = slow.next or head
                head = head.next.next
            mid = slow.next
            slow.next = None
            return mid

        def merge(l1, l2):
            dummy_head = ListNode()
            tail = dummy_head
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                    tail = tail.next
                else:
                    tail.next = l2
                    l2 = l2.next
                    tail = tail.next
            tail.next = l1 or l2
            return dummy_head.next

        if not head or not head.next:
            return head
        mid = find_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
