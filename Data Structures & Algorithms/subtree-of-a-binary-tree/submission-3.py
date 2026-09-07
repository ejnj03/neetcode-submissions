# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        recursive approach 
        O (M x N) time
        - each node can be each position in the subtree
        if: 
            - if no root but there is subRoot or vv:
                just return False ()

            - root and subRoot:
                - if both exist and values match:
                    compare left, left and right, right 
                try comparing left, subroot and right, subroot (left as root, right as root)
            
                
        """
        def isSame(n1, n2):
            """
            returns whether n1 and n2 contain the same tree
            """
            if not n1 and not n2:
                return True
            #both exist
            
            if n1 and n2 and n1.val == n2.val:
                #print(n1.val, n2.val)
                return isSame(n1.left, n2.left) and isSame(n1.right, n2.right)
            return False

        q = deque([root])
        while len(q) > 0:
            node = q.popleft()
            if isSame(node, subRoot):
                return True
            if node:
                q.append(node.left)
                q.append(node.right)
        return False 