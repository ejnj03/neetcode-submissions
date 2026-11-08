# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        highest = largest value seen so far 
        ret 0 if no node
        res = 0
        if highest <= node.val (has no anc > node): res += 1 
        highest = max(highest, node.val)

        """
        def DFS(node, highest):
            if not node: return 0
            res = 0
            if highest <= node.val:
                res += 1
            #print(node.val, highest, res)
            highest = max(highest, node.val)
            res += DFS(node.left, highest) + DFS(node.right, highest)
            return res

        return DFS(root, float('-inf'))