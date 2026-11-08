class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        cost to get to end from pos i 
        last idx = 0 
        maintain 3
        ways to get to pos i = from pos i - 1 and pos i - 2 
        min(cost to get to pos i - 1, i - 2) = min cost to get to pos i 
        """
        l = len(cost)
        if l <= 2:
            return min(cost)

        
        window = [cost[0], cost[1], 0]
        for i in range(2, l):
            window[i % 3] = cost[i] + min(window[(i - 1) % 3], window[(i - 2) % 3])
        return min(window[(l - 1) % 3], window[(l - 2) % 3])
