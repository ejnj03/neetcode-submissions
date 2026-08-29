# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        iterative DFS
        """
        if not root: return 0 
        stack, res = [(root, 1)], 1
        while len(stack) > 0:
            node, level = stack.pop()
            res = max(level, res)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return res
        