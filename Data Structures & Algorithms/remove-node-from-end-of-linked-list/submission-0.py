# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        f = start
        for _ in range(n+1): # target is distance n + 1 from the end (end = 1 + last node)
            f = f.next
        
        s = start
        while f:
            s, f = s.next, f.next
        
        s.next = s.next.next
        return start.next