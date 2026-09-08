# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        globally keep track of the res 
        - node = curr 
        - candidates:
            - a path for which highest node is the current node (includes current node) (vertex is the current node)
            
            - path in the left subtree
            - path in the right subtree 
            return path which includes this node + max of left or right subtree (vertex not this node )

        """

        res = float('-inf')

        def rec(curr):
            if not curr: return 0
            nonlocal res
            #max ps that includes the current node
            #print(curr.val)
            ls, rs = rec(curr.left), rec(curr.right)
            ps = curr.val + max(ls, 0) + max(rs, 0)
            res = max(ps, res)
            return curr.val + max(ls, rs, 0)
        
        rec(root)
        return res
