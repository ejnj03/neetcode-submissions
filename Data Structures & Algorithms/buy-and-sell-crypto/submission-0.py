class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        
        sell = prices[len(prices) - 1]
        #start, stop, step
        for buy_idx in range(len(prices) - 2, -1, -1):
            buy = prices[buy_idx]
            #update max profit
            prof = max(prof, sell - buy)
            #update max sell from max sell of subarray[buy:] to subarr[buy:]
            sell = max(buy, sell)
            #print(f"current buy: {buy}")
        return prof
