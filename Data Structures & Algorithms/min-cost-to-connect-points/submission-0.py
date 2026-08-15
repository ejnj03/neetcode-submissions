class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        
        #create adj list based on manhattan dists
        adj = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        print(adj)
        #Run Prims
        mheap = [[0, 0]]

        mcost = 0
        while True:
            print(mheap, visited, mcost)
            #all of the points are visited then return 
            if len(mheap) == 0 or len(visited) == len(points): break

            #remove min dist element
            dist, point = heapq.heappop(mheap)
            if point in visited: continue
            visited.add(point)
            mcost += dist
            for dist_nb, point_nb in adj[point]:
                if point_nb not in visited:
                    heapq.heappush(mheap, [dist_nb, point_nb])
        
        return mcost
            
            
            
            