# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def longestPath(node):
            """
            return longest branch starting at node
            """
            nonlocal longest
            if not node:
                return 0
            l, r = longestPath(node.left), longestPath(node.right)
            longest = max(l + r, longest)
            return 1 + max(l, r)

        longestPath(root)
        return longest