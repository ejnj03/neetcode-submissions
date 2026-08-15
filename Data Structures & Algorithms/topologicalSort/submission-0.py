class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(n)}
        for edge in edges:
            src, dst = edge
            adj[src].append(dst)

        print(adj)

        visited = set()
        ret = []

        def dfs(src, prev):
            print("running dfs on ", src)
            if src in visited: return True
            if src in prev: return False
            prev.add(src)
            for node in adj[src]:
                res = dfs(node, prev)
                if not res: return False 
            visited.add(src)
            ret.append(src)
            return True
            
    
        
        for node in range(n):
            res = dfs(node, set())
            if not res:
                return ret

        ret.reverse()
        return ret
        