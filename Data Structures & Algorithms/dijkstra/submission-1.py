class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        nodes = [[] for _ in range(n)]
        
        #first build an adjacency list 
        #store nb, distance
        for rel in edges:
            u, v, t = rel
            #in dist, node order
            nodes[u].append((t, v))

        print(nodes)

        #min time it takes for all nodes to recieve signal = 
        #max of (min dists to each node)
        dists = {i: -1 for i in range(n)}
        
        #starting node
        heap = [(0, src)]

        while True:
            if len(heap) == 0:
                break
            #get min node 
            dist, node = heapq.heappop(heap)
            print(f"dist: {dist}, node: {node}")
            #min distance to that node
            if dists[node] > -1: 
                continue
            dists[node] = dist
            #add its nbs to the queue if we dont alr have the min dist
            for nb in nodes[node]:
                if dists[nb[1]] == -1:
                    #dist from node to it + shortest dist from start -> nb passing through node
                    heapq.heappush(heap, (nb[0] + dist, nb[1]))
            print(heap)
        print(dists)
        return dists
            