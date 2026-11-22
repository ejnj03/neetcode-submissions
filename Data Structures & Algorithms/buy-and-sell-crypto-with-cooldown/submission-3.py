class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        space optimized 2D DP
        
        best profit that you can make starting on day i:
        
        #if has on day[i]:
        ()
        max(profit from not selling on day i = day[i + 1][has], profit from selling on day i = cost[i] + day[i + 2][not has]
        ㄴ can't do anything on day i + 1 (can't buy by rule, can't sell since doesnt have anything so profit on day i + 1 if we sell on day i must be 0. so profit from selling on day i = cost[i] (profit on day i) + 0 (profit on day i + 1) + day[i + 2][not has] (profit on day i + 2)
        day[i][has] = max(cost[i] + day[i + 1][not has], day[i + 1][has])
        #if not has on day[i]
        max(buy on day i: -cost[i] + day[i + 1][has], don't buy on day i: day[i + 1][not has])
        """
        counter =  [{"not_has": 0, "has": 0} for _ in range(3)]
        for i in range(len(prices) - 1, -1, -1):
            #if has can sell or not sell
            counter[i % 3]["has"] = max(prices[i] + 0 + counter[(i + 2) % 3]["not_has"], counter[(i + 1) % 3]["has"])
            #if not has can buy or not buy
            counter[i % 3]["not_has"] = max(-prices[i] + counter[(i + 1) % 3]["has"], counter[(i + 1) % 3]["not_has"])
        
        return counter[0]["not_has"]

        