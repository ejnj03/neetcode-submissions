class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ci = 0
        sz = min(strs, key=lambda x: len(x))
        while ci < len(sz):
            flag = False
            c = strs[0][ci]
            for si in range(1, len(strs)):
                print(f"{strs[si][:ci+1]}")
                if strs[si][ci] != c:
                    print("done")
                    flag = True
                    break
            if flag:
                break
            ci += 1
        return strs[0][:ci]