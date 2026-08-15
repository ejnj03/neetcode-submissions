class UnionFind:
    def __init__(self, n):
        self.num_nodes = n
        self.parents = [i for i in range(n)]
        self.lens = [1 for _ in range(n)]
        
    def find_root(self, i):
        #find root of the set containing the item
        parent = self.parents[i]
        if parent == i:
            return parent
        self.parents[i] = self.find_root(parent)
        return self.parents[i]

    def union(self, i, j):
        #path compress both
        root1 = self.find_root(i)
        root2 = self.find_root(j)
        if root1 == root2:
            return False
        if self.lens[root1] < self.lens[root2]:
            self.parents[root1] = root2
            self.lens[root2] += self.lens[root1]
        else:
            self.parents[root2] = root1
            self.lens[root1] += self.lens[root2]
        return True
    
    #def unique_roots(self, i, j):


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        q = []
        for ui, vi, wi in edges:
            heapq.heappush(q, (wi, ui, vi))
        
        uf = UnionFind(n)
        tot = 0
        curr = None

        while True:
            if len(q) == 0:
                break
            wi, ui, vi = heapq.heappop(q)
            if not uf.union(ui, vi):
                continue
            tot += wi
        
        return tot if max(uf.lens) == n else -1
