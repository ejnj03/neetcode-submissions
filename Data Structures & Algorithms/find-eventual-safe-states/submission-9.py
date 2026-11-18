class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degrees = [len(graph[node]) for node in range(n)]
        parents = [[] for _ in range(n)]
        for node in range(n):
            for child in graph[node]:
                parents[child].append(node)

        q = [node for node in range(n) if out_degrees[node] == 0]
        while len(q) > 0:
            node = q.pop()
            for parent in parents[node]:
                out_degrees[parent] -= 1
                if out_degrees[parent] == 0:
                    q.append(parent)
        
        return [node for node in range(n) if out_degrees[node] == 0]
