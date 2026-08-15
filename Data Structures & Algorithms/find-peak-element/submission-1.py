class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            left = float('-inf') if i < 1 else nums[i - 1]
            right = float('-inf') if i > len(nums) - 2 else nums[i + 1]
            if left < nums[i] and right < nums[i]:
                l = i
                break
            if right > nums[i]:
                l = i + 1
            else:
                r = i - 1
        
        return l