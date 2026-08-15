# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
        
    def num_nodes(self, node):
        #print(node.val)
        if not node.next:
            return node, 1
        l_n, count = self.num_nodes(node.next)
        return l_n, count + 1

    def reverse_half(self, node, count, prev):
        if not node:
            return
        next_node = node.next
        if count == self.split or count == self.split + 1:
            node.next = None
        elif count > self.split:
            node.next = prev
        #print(node.val, node.next.val if node.next else None)
        self.reverse_half(next_node, count + 1, node)

    def mergeLists(self, h1, h2):
        #starts with h1
        c1, c2 = h1, h2
        while c1 and c2:
            #print(c1.val, c2.val)
            #print("next: ", c1.next.val if c1.next else None, c2.next.val if c2.next else None)
            n1, n2 = c1.next, c2.next
            c1.next = c2
            c2.next = n1
            c1, c2 = n1, n2
        return h1

    def reorderList(self, head: Optional[ListNode]) -> None:
        #head is 1
        
        end, num = self.num_nodes(head)
        self.split = math.ceil(num/2)

        self.reverse_half(head, 1, None)

        #print(head.val, end.val)
        self.mergeLists(head, end)
        
                
            
            

        