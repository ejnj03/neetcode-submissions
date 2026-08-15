class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            #print(nums[l:r+1], nums[mid])
            if nums[mid] == target: return True
            elif nums[mid] == nums[l] and nums[mid] == nums[r]:
                l, r = l + 1, r - 1 #target can be in either half
            elif nums[mid] == nums[r]:
                r = mid - 1
            elif nums[mid] == nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]: #end - start idx between mid and l
                if target >= nums[l] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] > nums[r]:
                if target <= nums[r] or target > nums[mid]:
                    l = mid + 1 #mid ~ r contains target 
                else:
                    r = mid - 1
            else: #in order arr
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False
