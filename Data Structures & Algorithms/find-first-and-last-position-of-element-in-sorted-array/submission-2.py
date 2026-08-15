class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #bs twice, first to find start and then to find end
        
        def bs(l, r, first=True):
            while l <= r:
                
                mid = (l + r) // 2
                if first: #finding the first occurence
                    if target <= nums[mid]:
                        r = mid - 1
                    else: #target > nums[mid]
                        l = mid + 1
                else: #finding last occurence
                    if target >= nums[mid]:
                        l = mid + 1
                    else: #target < nums[mid]
                        r = mid - 1
                print(l, r)
            if first:
                if l < 0 or l > len(nums) - 1: return -1
                if nums[l] != target: return -1
            return l if first else r
        
        if len(nums) == 0: return [-1, -1]
        start = bs(0, len(nums) - 1)
        if start == -1:
            return [-1, -1]
        end = bs(0, len(nums) - 1, first=False)
        return [start, end]