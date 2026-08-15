class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[None for _ in range(n)] for _ in range(m)]
        memo[m-1][n-1] = 1
        print(memo)

        def memoi(row, col):
            if row > m-1 or col > n-1: return 0
            if obstacleGrid[row][col] == 1: return 0
            if not memo[row][col]:
                memo[row][col] = memoi(row + 1, col) + memoi(row, col + 1)
            return memo[row][col]

        return memoi(0,0)