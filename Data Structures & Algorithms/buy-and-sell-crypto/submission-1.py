class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        
        buy = prices[0]
        for sell_idx in range(1, len(prices)):
            sell = prices[sell_idx]
            #update max profit
            prof = max(prof, sell - buy)
            #update min sell from min sell of up to curr sell to to up and inc curr sell
            buy = min(buy, sell)
            #print(f"current buy: {buy}")
        return prof
