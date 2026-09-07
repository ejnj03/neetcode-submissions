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
                res += f"${node.val}$"
                res = serialize(node.left, res)
                res = serialize(node.right, res)
            else:
                res += "$_$"
            
            return res
        
        s1 = serialize(root, "")
        s2 = serialize(subRoot, "")
        if s2 in s1:
            return True
        return False
                