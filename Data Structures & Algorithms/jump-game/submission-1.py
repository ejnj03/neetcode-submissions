class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        DFS to ret on finding 1st solution
        """
        def dfs(i):
            nonlocal nums
            if i == len(nums) -1: return True
            if nums[i] == 0: return False #not final pos and 0
            val, nums[i] = nums[i], 0
            res = False
            for offset in range(1, min(val, len(nums) - 1 - i) + 1):
                res |= dfs(i + offset)
            return res
        
        return dfs(0)