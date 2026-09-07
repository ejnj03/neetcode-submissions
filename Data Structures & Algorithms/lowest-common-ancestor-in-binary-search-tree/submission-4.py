# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        lowest node st subtree contains both p and q
        lca: the node whose value is between p and q
        - given current node curr:
            if both smaller than curr:
                both in left subtree
            if both larger than curr:
                both in right subtree
            if (one is smaller and one is larger) or either is = to curr:
                curr node is the lca
        """
        #given that p != q
        sm, lg, curr = min(p.val, q.val), max(p.val, q.val), root

        while curr:
            if lg < curr.val:
                curr = curr.left
            elif sm > curr.val:
                curr = curr.right
            #if lg == curr.val or sm == curr.val or (lg > curr.val and sm < curr.val): 
            else:
                return curr

        return None
        
