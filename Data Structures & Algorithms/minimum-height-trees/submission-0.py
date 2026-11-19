class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        longest path - store path 
        
        in order traversal (c1, Root, c2)
        want to find middle nodes of the longest path (1 for odd, 2 for even)
        """
        
        #create adjacency list 
        nbs = defaultdict(list)
        for ai, bi in edges:
            nbs[ai].append(bi)
            nbs[bi].append(ai)
        counts = [len(nbs[node]) for node in range(n)]
        
        unvisited = set([i for i in range(n)]) #avoid cycles (going from parent - child - parent)
        q = [node for node in range(n) if len(nbs[node]) == 1]
        q_next = []
        while len(unvisited) > 2:
            while len(q) > 0:
                node = q.pop()
                unvisited.remove(node) #mark visited
                for nb in nbs[node]:
                    if nb in unvisited:
                        counts[nb] -= 1 #prune node 
                        if counts[nb] == 1:
                            q_next.append(nb)
            q, q_next = q_next, []     
               
        return list(unvisited)

        