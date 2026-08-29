class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 3 4 5 1 2 3 
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target: 
                return mid
            if nums[l] <= nums[mid]: #left side is the sorted side 
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1 #target is in left side
                else:
                    l = mid + 1
            else: #right side is the sorted side (mid < r)
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return mid if nums[mid] == target else -1

                