class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.tot = sum(w)
        prev = 0
        for wi in range(len(w)):
            self.w[wi] += prev
            prev = self.w[wi]
        print(w)

    def pickIndex(self) -> int:
        chosen = random.randint(1, self.tot)
        print(f"chosen: {chosen}")
        #binary search
        l = 0
        r = len(self.w) - 1
        res = None
        while l < r:
            mid = (l + r) // 2
            bound = self.w[mid]
            print(f"bound: {bound}")
            if bound > chosen:
                r = mid
            elif bound < chosen:
                l = mid + 1
            else:
                r = mid
                l = mid
                break
        return r
                
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()