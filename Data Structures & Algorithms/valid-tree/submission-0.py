class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [i for i in range(n)] #parent
        self.r = [1 for _ in range(n)] #rank
    
    def union(self, u, v) -> bool:
        """
        add edge to graph
        returns false if creating edge would create cycle
        """
        ru, rv = self.find_root(u), self.find_root(v)

        if ru == rv: return False
        if self.r[ru] > rv:
            self.p[rv] = ru
        elif self.r[rv] > ru:
            self.p[ru] = rv
        else: #same degree
            self.p[rv] = ru
            self.r[ru] += 1 #adds chain of len n to ru (rank n -> n + 1)
        return True

    def find_root(self, u) -> int:
        """
        return parent; path compress in the process
        """
        curr = u
        while self.p[curr] != curr: #root's parent is itself
            curr, self.p[curr] = self.p[curr], self.p[self.p[curr]]
        return curr
    
    def num_components(self) -> int:
        """
        returns the number of connected components in the uf graph
        """
        roots = set()
        for i in range(self.n):
            roots.add(self.find_root(i))
        return len(roots)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        valid tree conditions: 
        - every node should be connected (only single union)
        - there should be no cycles
        
        use uf to find cycles 
            - i.e., if u, v already have the same parent (are part of the same tree) then this edge would create a cycle
        """
        uf = UnionFind(n)
        for i, j in edges:
            if not uf.union(i, j):
                return False
        if uf.num_components() != 1: return False
        return True 
            
            
        