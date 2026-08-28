class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * (n) #number of children 

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

    def getNumComponents(self) -> int:
        res = set()
        for par in self.parent:
            res.add(self.find(par))
        return len(res)

