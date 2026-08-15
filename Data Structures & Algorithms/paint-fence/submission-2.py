class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        prev[0]: prev is same 
        prev[1]: prev is diff
        """
        
        #up to pos 0
        prev = [0, k]

        #start at pos 1
        for pos in range(1, n):
            #prev is same -> pos must be diff
            curr = [0, 0]
            #prev is diff -> can be diff
            curr[1] = prev[0] * (k - 1) + prev[1] * (k - 1)
            #prev is diff -> can be same
            curr[0] = prev[1] * 1
            prev = curr
        
        return sum(prev)
        
        
        