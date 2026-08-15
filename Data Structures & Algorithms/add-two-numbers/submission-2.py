# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_number(n1, n2, overflow=False, prev=None):
            if not n1 and not n2:
                if overflow:
                    prev.next = ListNode(val=1)
                return
            if not n1:
                n1 = ListNode(val=0)
                prev.next = n1
            if not n2:
                n2 = ListNode(val=0)
            ps = 0
            if overflow:
                ps += 1
            overflow = False #reset
            #print(ps, n1.val, n2.val)
            ps += n1.val + n2.val
            if ps >= 10:
                ps -= 10
                overflow=True
            n1.val = ps

            get_number(n1.next, n2.next, overflow, n1)
        
        get_number(l1, l2)
        return l1

