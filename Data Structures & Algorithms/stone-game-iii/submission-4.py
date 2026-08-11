class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        L = len(stoneValue)

        if L == 1:
            return "Alice" if stoneValue[0] > 0 else "Bob" if stoneValue[0] < 0 else "Tie"

        for i in range(L - 2, -1, -1):
            stoneValue[i] += stoneValue[i + 1]
        ss = stoneValue

        # [F(i - 3), F(i - 2), F(i - 1)]
        # init: F(L - 2), F(L - 1), F(L)
        curr = [max(ss[L - 2], ss[L - 2] - ss[L - 1]), ss[L - 1], 0]
        #print(curr)
        idx = L - 3
        while (idx >= 0):
            #F(i)
            score = ss[idx] - min(curr)
            curr = [score, curr[0], curr[1]]
            #print(curr)
            idx -= 1
        
        mid = ss[0] / 2
        #print(mid)
        return "Alice" if curr[0] > mid else "Bob" if curr[0] < mid else "Tie"
        
        