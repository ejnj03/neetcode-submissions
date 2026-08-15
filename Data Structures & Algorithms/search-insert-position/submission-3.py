class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0
        while l <= r:
            p = (l + r) // 2
            if nums[p] == target:
                return p
            if target > nums[p]:
                l = p + 1
            else:
                r = p - 1
        return l