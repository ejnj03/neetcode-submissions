class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        2D DP (non space optimized solution)
        """
        rs, cs = len(grid), len(grid[0])
        costs = [[-1 for _ in range(cs)] for _ in range(rs)]
        
        def min_cost(r, c):
            """
            return min cost when starting at position r, c
            """
            if r > rs -1 or c > cs - 1: return float('inf')
            if r == rs - 1 and c == cs - 1: #at dst
                return grid[r][c]
            if costs[r][c] == -1:
                costs[r][c] = grid[r][c] + min(min_cost(r + 1, c), min_cost(r, c + 1))
            return costs[r][c]
            
        
        return min_cost(0, 0)