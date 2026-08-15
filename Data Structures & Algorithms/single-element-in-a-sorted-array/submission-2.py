class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            #prior to occurence even = even + 1 (odd)
            is_odd = True if mid % 2 == 1 else False

            #0 is even so will not check out of bounds 
            if (is_odd and nums[mid - 1] == nums[mid]) or (not is_odd and nums[mid] == nums[mid + 1]):
                #proper behavior so skip occured at a later index
                l = mid + 1
            else:
                left_valid = mid < 1 or nums[mid - 1] != nums[mid]
                right_valid = mid > len(nums) - 2 or nums[mid + 1] != nums[mid]
                if right_valid and left_valid:
                    r = mid
                    break
                #occured before mid
                r = mid - 1
            
            print(l, r)

        
        return nums[r]
                
                