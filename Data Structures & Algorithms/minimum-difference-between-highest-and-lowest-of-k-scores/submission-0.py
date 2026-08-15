class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = float('inf')
        l = 0
        
        while l + k - 1 < len(nums):
            r = l + k - 1
            diff = min(diff, nums[r] - nums[l])
            l += 1
    
        return diff
            