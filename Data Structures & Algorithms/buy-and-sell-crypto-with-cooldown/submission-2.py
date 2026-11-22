class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        recursive (brute force) solution:
        explore all possible paths 
        state representation: (has_coin, curr_profit)
        """
        counter =  [{True: -1, False: -1} for _ in range(len(prices))]
    
        def rec(i, has_coin):
            """
            return best profit
            """
            if i > len(prices) - 1: return 0
            if counter[i][has_coin] > -1:
                return counter[i][has_coin]
            best = float('-inf')
            if i > 0 and has_coin: #can't sell at i = 0, and if X have coin 
                #sell
                best = max(best, rec(i + 2, False) + prices[i])
            if i < len(prices) - 1 and not has_coin: #no point of buying at last idx, can't buy if X have coin
                best = max(best, rec(i + 1, True) - prices[i])
            #do nothing option
            best = max(best, rec(i + 1, has_coin))
            counter[i][has_coin] = best
            return best

        return rec(0, False)
            
                
        