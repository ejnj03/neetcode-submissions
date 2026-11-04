# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def longestPath(node):
            """
            return longest branch starting at node
            """
            if not node:
                return 0
            l, r = longestPath(node.left), longestPath(node.right)
            if l < 0 or r < 0: return -1 #if either the l or r is not a balanced bt
            if abs(l - r) > 1: return -1 #if curr is not a balanced bt
            return 1 + max(l, r)
        
        res = longestPath(root)
        return False if res < 0 else True
        

        