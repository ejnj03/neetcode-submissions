class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # ** CONSTANT space since alphabet is 26 chars so at most 26 distinct keys
        #(chars) in the dict 
        targets = [0] * 26
        for s in s1:
            targets[ord(s) - ord('a')] += 1
        
        l = 0
        r = 0
        counts = [0] * 26

        while l < len(s2):
            lc = ord(s2[l]) - ord('a')
            if targets[lc] == 0:
                l += 1
                continue
            if r < l:
                r = l
            while r < len(s2):
                rc = ord(s2[r]) - ord('a')
                if targets[rc] == 0 or counts[rc] >= targets[rc]:
                    break
                counts[rc] += 1
                r += 1

            if r - l == len(s1):
                return True

            counts[lc] -= 1
            l += 1
            
        return False