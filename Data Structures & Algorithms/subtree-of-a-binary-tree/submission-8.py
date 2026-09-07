# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        using pattern matching (O(m + n))
        """
        
        def serialize(node, res):
            if node:
                res.append(f"${node.val}")
                serialize(node.left, res)
                serialize(node.right, res)
            else:
                res.append("$_")
        
        s1, s2 = [], []
        serialize(root, s1)
        serialize(subRoot, s2)
        s1, s2 = "".join(s1), "".join(s2)
        if s2 in s1:
            return True
        return False
                