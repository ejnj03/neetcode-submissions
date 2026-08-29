# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def rec(node):
            if not node: return 0
            child = max(rec(node.left), rec(node.right))
            return 1 + child
        return rec(root)