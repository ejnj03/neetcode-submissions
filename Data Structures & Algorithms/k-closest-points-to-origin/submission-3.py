class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(math.sqrt(x**2 + y**2), (x, y)) for (x, y) in points]
        #print(dists)
        q = dists[:k]
        heapq.heapify_max(q)

        for i in range(k, len(points)):
            if q[0][0] > dists[i][0]:
                heapq.heappop_max(q)
                heapq.heappush_max(q, dists[i])
                #print(q)
        
        return [elem[1] for elem in q]


