class Solution:
    """
    provided optimal solution
    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)))
            res += ('#')
            res += (s)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            #exists at first "#"
            size = int(s[i:j])
            res.append(s[j + 1:j + 1 + size])
            i = j + 1 + size
        return res







