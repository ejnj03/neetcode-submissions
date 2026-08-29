class Solution:
    def climbStairs(self, n: int) -> int:
        curr = [0, 1, 2]
        i = 3
        
        while i <= n:
            curr[i % 3] = curr[(i % 3) - 1] + curr[(i % 3) - 2]
            i += 1
        
        return curr[n % 3]
        