# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS 
        """
        q, level = deque(), 0
        if root:
            q.append(root)
        while len(q) > 0:
            level += 1
            #pop each node in current level and append its children
            for i in range(len(q)): 
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
        return level
        