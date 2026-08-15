class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            #count excluding last bit + last bit count (1 if lb is 1 else 0)
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp
