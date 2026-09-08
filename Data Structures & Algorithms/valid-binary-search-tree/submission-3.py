# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def rec(node, lb, ub):
            if not node:
                return True
            #print(node.val, lb, ub)
            val = node.val
            if val <= lb or val >= ub: return False
            #val bounds: (lb, ub)
            #l: (lb, val) 
            #r: (val, ub) 
            l, r = rec(node.left, lb, val), rec(node.right, val, ub)
            return l and r

        #set to left and is smaller than pval regardless of what root is
        return rec(root, float('-inf'), float('inf'))
