"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nmap = {}
        
        #1. create copies
        curr = head
        while curr:
            nmap[curr] = Node(curr.val)
            curr = curr.next
        
        #2. assign random and next ptrs
        curr = head
        while curr:
            if curr.next:
                nmap[curr].next = nmap[curr.next]
            if curr.random:
                nmap[curr].random = nmap[curr.random]
            curr = curr.next
        
        return nmap[head] if head is not None else None
