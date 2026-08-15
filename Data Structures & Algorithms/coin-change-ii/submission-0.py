class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amounts = [1 if i == 0 else 0 for i in range(amount + 1)]
        
        for div in coins:
            for val in range(amount + 1):
                if val >= div:
                    amounts[val] += amounts[val - div]
        
        return amounts[-1]
            