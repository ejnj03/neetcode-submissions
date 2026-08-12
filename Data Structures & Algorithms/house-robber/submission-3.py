class Solution:
    #bottom up approach
    def rob(self, nums: List[int]) -> int:
        memo = [0, 0, 0]

        i = len(nums) - 1

        while i > -1:
            #replaces entry at (i + 3) % 3 (= i % 3)
            memo[i % 3] = max(nums[i] + memo[(i + 2) % 3], 0 + memo[(i + 1) % 3])
            i-= 1
        
        return memo[0] 

        