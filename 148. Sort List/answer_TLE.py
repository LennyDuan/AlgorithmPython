# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        sorted_res = sorted(res)

        def construct_list(res):
            if not res:
                return
            current_val = res.pop(0)
            node = ListNode(current_val)
            next_node = construct_list(res)
            node.next = next_node
            return node
        new_list = construct_list(sorted_res)
        print(new_list)
        return new_list
