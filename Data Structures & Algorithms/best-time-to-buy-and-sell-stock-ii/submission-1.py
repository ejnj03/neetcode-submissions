class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0

        for curr in range(1, len(prices)):
            if prices[curr] <= prices[curr - 1]:
                continue 
            curr_profit += prices[curr] - prices[curr - 1]
            curr += 1
        
        return curr_profit