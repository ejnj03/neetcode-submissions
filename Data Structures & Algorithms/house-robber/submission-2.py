class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def F(i):
            if i == len(nums) - 1: return nums[i]
            if i > len(nums) - 1: return 0
            if i in memo: return memo[i]
            
            res = max(nums[i] + F(i + 2), 0 + F(i + 1))
            memo[i] = res
            return res
        
        return F(0)