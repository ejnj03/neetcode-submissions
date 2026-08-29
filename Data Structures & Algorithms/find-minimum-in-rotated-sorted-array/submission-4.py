class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r] or r == l: #current array is sorted
                break
            mid = (r + l) // 2
            if nums[l] > nums[mid]: 
                r = mid
            else:
                l = mid + 1
        
        return nums[l] 
            
            
        