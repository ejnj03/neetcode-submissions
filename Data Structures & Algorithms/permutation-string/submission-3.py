class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targets = defaultdict(int)

        for s in s1:
            targets[s] += 1
        
        l = 0
        r = 0
        counts = defaultdict(int)
        while l < len(s2):
            if s2[l] not in targets:
                l += 1
                continue
            if r < l:
                r = l
            print(f"left {l}")
            while r < len(s2) and s2[r] in targets:
                if counts[s2[r]] >= targets[s2[r]]:
                    break
                counts[s2[r]] += 1
                r += 1
                print(s2[l:r+1])
            if r - l == len(s1):
                return True
            counts[s2[l]] -= 1
            l += 1
            
        return False