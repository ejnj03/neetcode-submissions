class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        prev = [0 if i == 0 else float('inf') for i in range(amount + 1)]
        
        for coin in coins:
            curr = prev.copy()
            for rem in range(amount + 1):
                if coin <= rem:
                    curr[rem] = min(curr[rem], 1 + curr[rem - coin])

            print(coin, prev)
            prev = curr
        
        return prev[amount] if prev[amount] != float('inf') else -1