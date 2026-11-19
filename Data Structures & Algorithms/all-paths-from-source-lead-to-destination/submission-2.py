class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        we don't care about nodes upstream of source

        start at source node
        - if path leads to dst: ret T
        - if path leads to cycle (already visited node)

        - keep global all_visited to track all visited nodes (don't run dst on one node twice) (skips if in this set)
        - keep local/call specific visited to track all the nodes that constitute the current path (to track/find cycles) (returns false if in this set)
        """
        #node : parents
        dst_nodes = [[] for _ in range(n)]
        for par, child in edges:
            dst_nodes[par].append(child)
        
        if len(dst_nodes[destination]) > 0 or source in dst_nodes[source]: return False
        all_visited = set()
        
        def dfs(node, visited):
            """
            return: whether downstream contains dst as end node
            """
            #return true if this is the dst node (we are given that dst has no children)
            if node == destination: return True
            if len(dst_nodes[node]) == 0: return False #if not dst but end of path
            verdict = True
            all_visited.add(node)
            visited.add(node)
            print(node, " current path: ", visited, " children: ", dst_nodes[node])
            for nb in dst_nodes[node]:
                if nb in visited: #
                    verdict = False
                elif nb not in all_visited: #was not visited by another path (not this one) and not dst
                    verdict = dfs(nb, visited)
                if verdict is False: break
            visited.remove(node) #when returning to the parent node
            print(verdict)
            return verdict
        

        return dfs(source, set())