class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            #print(nums[l:r+1], nums[mid])
            if nums[mid] == target: return True
            elif nums[mid] == nums[l] and nums[mid] == nums[r]:
                l, r = l + 1, r - 1 #target can be in either half
            elif nums[l] <= nums[mid]: # know left half is sorted for sure if nums[l] <= nums[mid]
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: #nums[r] >= nums[mid]
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
