# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        res = []
        while len(q) > 0:
            node = q.popleft()
            if node:
                res.append(f"${node.val}")
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("$_")
        return "".join(res)
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        in while loop: 
            add all the children on the next level to curr, and give all nodes in prev a connection to their children
            - prev: the current non-None parent nodes on a level 
                (the nodes that get a children in the current loop)
        
            if the children are not "_" -> create and add them to curr
                - curr: fill with the children of parent that are not None
        
        update prev to curr
            
        """
        #0th index is placeholder ('' because $ comes after it)
        data = deque(data.split("$")[1:])
        if data[0] == "_":
            return None
        root = TreeNode(int(data.popleft()))
        prev, curr = deque([root]), deque()

        while len(data) > 0:
            num_children = len(prev) * 2
            while len(prev) > 0: 
                
                node = prev.popleft()
                lval = data.popleft()
                rval = data.popleft()
                if lval != "_":
                    node.left = TreeNode(int(lval))
                    curr.append(node.left)
                if rval != "_":
                    node.right = TreeNode(int(rval))
                    curr.append(node.right)
            prev = curr

        return root


        