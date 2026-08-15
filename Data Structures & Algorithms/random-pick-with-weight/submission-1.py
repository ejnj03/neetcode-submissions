class Solution:

    def __init__(self, w: List[int]):
        self.w = w

        tot = sum(w)
        prev = 0
        for wi in range(len(self.w)):
            pi = (w[wi] / tot) * 100
            #range (prev, prev + pi] (i.e., [1, 20])
            self.w[wi] = prev + pi
            prev = self.w[wi]
        print(self.w)

    def pickIndex(self) -> int:
        chosen = random.randint(1, 100)
        idx = 0
        prev = 0
        while idx < len(self.w):
            curr = self.w[idx]
            if chosen > prev and chosen <= curr:
                return idx
            idx += 1
            prev = curr


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()