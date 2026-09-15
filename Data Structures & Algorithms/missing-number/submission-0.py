class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(list(range(len(nums) + 1)))

        for n in nums:
            total -= n
        return total
        