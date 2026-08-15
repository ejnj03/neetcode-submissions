class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = {i: {} for i in range(n)}
        #val: edge idx, edge weight, nb

        for edge_idx in range(len(edges)):
            ai, bi, wi = edges[edge_idx]
            adj[ai][bi] = wi
            adj[bi][ai] = wi

        print(adj)

        
        #first just find the solution
        ceil = 1000
        floor = 1

        def mst():
            cost = 0
            q=[(0, 0)]

            visited = set()

            while True:
                #print(f"queue state: {q}")
                #print(f"used: {used}, visited nodes: {visited}")
                if len(visited) == n or len(q) == 0:
                    return cost, len(visited)
                w, v = heapq.heappop(q)
                if v in visited or w > ceil: continue
                visited.add(v)
                cost += w

                for nbv, nbw in adj[v].items():
                    if nbv in visited or nbw > ceil: continue
                    heapq.heappush(q, (nbw, nbv))
                
        cost, visited_n = mst()
        non_critical = set()
        critical = set()
        #find which of these are non essential nodes
        
        for i in range(len(edges)):
            #check if is critical
            ai, bi, wi = edges[i]

            #set weight to ceil so its never chosen
            adj[ai][bi] = 2000
            adj[bi][ai] = 2000
            exc_cost, exc_visited = mst()
            if exc_visited < n or exc_cost > cost:
                #if without this edge we get no mst (not min or not tree)
                critical.add(i)
            else:
                #check if it can be in mst
                adj[ai][bi] = 0
                adj[ai][bi] = 0
                exc_cost, exc_visited = mst()
                if exc_visited == n and exc_cost + wi == cost:
                    non_critical.add(i)
            #set it back
            adj[ai][bi] = wi
            adj[bi][ai] = wi

        
        return [list(critical), list(non_critical)]