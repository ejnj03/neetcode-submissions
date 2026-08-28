class UnionFind:
    
    def __init__(self, arr):
        self.elems = set(arr)
        self.parent = {num: num for num in self.elems}
        self.rank = {num: 1 for num in self.elems} #number of children 

    def find(self, x: int) -> int:
        curr = x
        while self.parent[curr] != curr:
            par = self.parent[curr]
            #child of parent (curr) becomes sibling
            self.parent[curr] = self.parent[par]
            curr = par
        return curr

    def isSameComponent(self, x: int, y: int) -> bool:
        rootx, rooty = self.find(x), self.find(y)
        return True if rootx == rooty else False

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y): return False
        rootx, rooty = self.find(x), self.find(y)
        rankx, ranky = self.rank[rootx], self.rank[rooty]
        if rankx > ranky:
            #rank of rooty is smaller (y becoming subtree of x doesnt add rank to x)
            self.parent[rooty] = rootx
        elif ranky > rankx:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
        return True 

    def getCounts(self) -> int:
        counts = defaultdict(int)
        print(self.parent)
        for par in self.parent:
            #add count to its root 
            counts[self.find(par)] += 1 
        return counts

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        uf = UnionFind(nums)
        for num in list(uf.elems):
            if num - 1 in uf.elems:
                uf.union(num - 1, num)
        return max(uf.getCounts().values())
