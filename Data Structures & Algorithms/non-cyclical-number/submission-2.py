class Solution:
    def sosq(self, n) -> int:
        return sum([int(d) ** 2 for d in str(n)])
    def isHappy(self, n: int) -> bool:
        """
        fast and slow pointers (what I remember)
            s: moves by one 
            f: moves by two
            if there's a cycle: they'll meet before you iterate through the entire list more than once
        ㄴ don't need to keep track of every number you've seen -> memory goes to O(1)
        n -> sum of sq of digits -> ... -> 
        """
        s = self.sosq(n)
        f = self.sosq(self.sosq(n))
        while True:
            if s == 1 or f == 1: return True 
            if s == f: return False
            s = self.sosq(s)
            f = self.sosq(self.sosq(f))
            
        