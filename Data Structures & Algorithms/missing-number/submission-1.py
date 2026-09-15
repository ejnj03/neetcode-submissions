class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            add, subtract = i, nums[i]
            total += add - subtract
        #total expected sum - total array sum
        return total + len(nums)
        