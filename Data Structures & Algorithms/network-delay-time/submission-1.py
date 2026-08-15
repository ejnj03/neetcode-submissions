class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = [[] for _ in range(n+1)]
        
        #first build an adjacency list 
        #store nb, distance
        for rel in times:
            u, v, t = rel
            #in dist, node order
            nodes[u].append((t, v))

        print(nodes)

        #min time it takes for all nodes to recieve signal = 
        #max of (min dists to each node)
        dists = [float('inf') for _ in range(n+1)]
        
        #starting node
        heap = [(0, k)]

        while True:
            if len(heap) == 0:
                break
            #get min node 
            dist, node = heapq.heappop(heap)
            print(f"dist: {dist}, node: {node}")
            #min distance to that node
            if dists[node] < float('inf'): 
                continue
            dists[node] = min(dist, dists[node])
            #add its nbs to the queue if we dont alr have the min dist
            for nb in nodes[node]:
                if dists[nb[1]] == float('inf'):
                    #dist from node to it + shortest dist from start -> nb passing through node
                    heapq.heappush(heap, (nb[0] + dist, nb[1]))
            print(heap)
        print(dists)
        return -1 if float('inf') in dists[1:] else max(dists[1:])
            