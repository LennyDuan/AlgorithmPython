class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        from collections import defaultdict
        copy = defaultdict(lambda: Node(0, None, None))
        copy[None] = None

        curr = head
        while curr:
            copy[curr].val = curr.val
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return copy[head]

