class Solution:
    #bottom up
    """
    not circular give the best solution amongst candidates, including 
    the candidate that contains both the first and last element.

    we want the best candidate excluding the candidate that contains the first and last element.

    so we compare the best candidate of all candidates that exclude index -1
    against the best candidate of all candidates that excludes index 0
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def robber(start, end) -> int:
            memo = [0, 0, 0]
            i = end

            while i > start-1:
                #replaces entry at (i + 3) % 3 (= i % 3)
                memo[i % 3] = max(nums[i] + memo[(i + 2) % 3], 0 + memo[(i + 1) % 3])
                i-= 1
            return memo[start % 3]
        return max(robber(0, len(nums) - 2), robber(1, len(nums) - 1))
