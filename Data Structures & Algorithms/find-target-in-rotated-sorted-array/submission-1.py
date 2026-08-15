class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(start_idx, end_idx):
            print(nums[start_idx: end_idx + 1])
            #lower of the 2 indices (i.e., size 6 arr => 2)
            mid = (end_idx - start_idx) // 2 + start_idx
            if nums[mid] == target:
                return mid
            if start_idx >= end_idx:
                return -1
            #recurse on the array containing wrapped segment
            print(nums[mid])
            if nums[mid] > nums[end_idx] and (target > nums[mid] or target <= nums[end_idx]):
                return bs(mid + 1, end_idx)
            elif nums[mid] < nums[end_idx] and (target > nums[mid] and target <= nums[end_idx]):
                return bs(mid + 1, end_idx)
            else:
                #no wrap or wrapped is part of 1st seq
                return bs(start_idx, mid - 1)
        return bs(0, len(nums) - 1)