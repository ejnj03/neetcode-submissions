class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        for i in range(len(piles) - 2, -1, -1):
            piles[i] = piles[i + 1] + piles[i]

        memo = {}
        #returns the maximum score player can get at current state
        #assuming that other player also plays optimally
        def dp(i, M): 
            #print(i, M)
            if (i, M) in memo:
                return memo[(i, M)]
            #base case 
            if 2 * M >= len(piles) - i:
                return piles[i]
            
            res = 0
            for x in range(1, 2 * M + 1):
                res = max(res, piles[i] - dp(i + x, max(x, M)))
            
            memo[(i, M)] = res
            return res

        return dp(0, 1)

            
            