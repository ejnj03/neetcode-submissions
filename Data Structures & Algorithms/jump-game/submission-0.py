class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        DFS to ret on finding 1st solution
        """
        visited = set()
        def dfs(i):
            nonlocal visited, nums
            if i == len(nums) -1: return True
            if nums[i] == 0: return False #not final pos and 0
            visited.add(i)
            res = False
            for offset in range(1, min(nums[i], len(nums) - 1 - i) + 1):
                if i + offset not in visited:
                    res |= dfs(i + offset)
            return res
        
        return dfs(0)