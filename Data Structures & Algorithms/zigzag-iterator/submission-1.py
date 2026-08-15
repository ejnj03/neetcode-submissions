class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vs = [v1, v2]
        #track arrays done or rem
        self.done = [0 if len(arr) > 0 else 1 for arr in self.vs]
        #current active arr
        self.curr = 0 if self.done[0] == 0 else 1
        #track current idx of each arr
        self.idxs = [0, 0]

    def next(self) -> int:
        if not self.hasNext():
            return 
        #current arr
        curr = self.curr
        arr = self.vs[curr]
        idx = self.idxs[curr]

        print(f"curr arr: {curr} array state: {arr} curr idx: {idx}")
        self.idxs[curr] += 1

        if self.idxs[curr] >= len(arr):
            self.done[curr] = 1
        #if other array is not done
        other_arr = self.curr ^ 1
        if not self.done[other_arr]:
            self.curr = other_arr
        
        return arr[idx]

    def hasNext(self) -> bool:
        res = self.done[0] ^ 1 or self.done[1] ^ 1
        print(res)
        return res

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
