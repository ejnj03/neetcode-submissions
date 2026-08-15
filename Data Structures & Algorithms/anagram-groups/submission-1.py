class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        base = ord('a')
        for s in strs:
            cs = [0] * 26
            for c in s:
                cs[ord(c) - base] += 1
            print(cs)
            rep = " ".join([str(i) for i in cs])
            print(rep)
            groups[rep].append(s)
        
        return list(groups.values())
                    