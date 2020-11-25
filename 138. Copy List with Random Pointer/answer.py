class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        deep_copy = Node(head.val)
        origin_head = head

        def find_copy_node(copy_head, val):
            while copy_head:
                if copy_head.val is val:
                    return copy_head
                copy_head = copy_head.next

        while head and head.next:
            current_deep_copy = find_copy_node(deep_copy, head.val)
            current_deep_copy.next = Node(head.next.val)
            head = head.next

        while origin_head:
            current_deep_copy = find_copy_node(deep_copy, origin_head.val)
            if origin_head.random is None:
                current_deep_copy.random = None
            else:
                current_deep_copy.random = find_copy_node(deep_copy, origin_head.random.val)
            origin_head = origin_head.next or None

        return deep_copy
