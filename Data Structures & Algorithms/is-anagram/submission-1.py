#from collections 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s_c = set()
        s_c = defaultdict(int)
        for c in s:
            #s_c.add(c)
            s_c[c] += 1

        for c in t:
            if s_c[c] == 0:
                return False
            s_c[c] -= 1
        return True if sum(s_c.values()) == 0 else False