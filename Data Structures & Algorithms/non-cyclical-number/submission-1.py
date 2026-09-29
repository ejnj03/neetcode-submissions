class Solution:
    def isHappy(self, n: int) -> bool:
        seen, curr = set(), n
        while True:
            if curr in seen: return False
            if curr == 1: return True 
            seen.add(curr)
            curr = sum([int(d) ** 2 for d in str(curr)])
        
            