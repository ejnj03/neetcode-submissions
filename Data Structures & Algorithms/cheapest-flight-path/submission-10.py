class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        
        """
        adj = defaultdict(list)
        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))
        
        stops = [k + 1] * n #every path to dst should be < k stops 
        #costs = [float('inf')] * n
        heap = [(0, 0, src)] #cost, stops, node

        while len(heap) > 0:
            cost, stop, node = heapq.heappop(heap)
            if stop >= stops[node]:
                continue 
            stops[node] = stop
            if node == dst:
                return cost
            #print(cost, stop, node)
            #update cost
            #costs[node] = min(costs[node], cost)
            for nb, price in adj[node]:
                nb_stops = stop + 1 if nb != dst else stop
                if nb_stops < stops[nb]: #less stops to this node than previously explored paths
                    heapq.heappush(heap, (cost + price, nb_stops, nb))
            #print(heap)
            #print(stops, costs)
        
        return -1
                    