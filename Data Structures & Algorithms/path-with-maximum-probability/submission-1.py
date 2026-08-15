class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        nodes = [[] for _ in range(n)]
        for p, edge in zip(succProb, edges):
            a, b = edge
            nodes[a].append((p, b))
            nodes[b].append((p, a))
        
        visited = set()
        frontier = [(-1, start_node)]
        while True:
            if len(frontier) == 0:
                break
            p, node = heapq.heappop(frontier)
            print(f"p: {p} node: {node}")
            if node == end_node:
                #make it positive again
                return -1 * p
            elif node in visited:
                continue
            #add it to visited
            visited.add(node)
            #iterate over its nbs
            for p_nb, nb in nodes[node]:
                if nb in visited:
                    continue
                heapq.heappush(frontier, ((p_nb * p), nb))
        return 0