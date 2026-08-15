class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        prev = [0 for cap in range(capacity + 1)]
        print(prev)
        
        for last_item in range(len(weight)):
            curr = [0 for _ in range(capacity + 1)]
            
            for cap in range(capacity + 1):
                #max profit without current item for using items up to current item
                curr[cap] = prev[cap]
                #if can't include current item based on current capcity then include X possible
                include = 0
                #if can include:
                if weight[last_item] <= cap:
                    #max profit at c = profit for pi + max profit at c - wi
                    #since weight <= cap, its guarenteed that we alr updated 
                    include = profit[last_item] + curr[cap - weight[last_item]]
                curr[cap] = max(include, curr[cap])
            
            prev = curr
        
        return prev[capacity]