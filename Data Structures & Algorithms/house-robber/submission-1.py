class Solution:
    def rob(self, nums: List[int]) -> int:
        #memo[i]: max amt of money that can be made from robbing this house and onwards
        memo = [None for i in range(len(nums))]

        def memoi(i):
            if i >= len(nums): return 0
            if memo[i]:
                return memo[i]
            val = max(nums[i] + memoi(i+2), memoi(i+1))
            memo[i] = val
            return val

        for num in range(len(nums)):
            memoi(num)
        
        print(nums)
        print(memo)
        return max(memo)