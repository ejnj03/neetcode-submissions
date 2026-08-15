class Solution:
    def findMin(self, nums: List[int]) -> int:
        curr = float('inf')
        def bs(start_idx, end_idx):
            nonlocal curr
            print(nums[start_idx: end_idx + 1])
            #lower of the 2 indices (i.e., size 6 arr => 2)
            mid = (end_idx - start_idx) // 2 + start_idx
            curr = min(nums[mid], curr)
            if start_idx >= end_idx:
                return
            #recurse on the array containing wrapped segment
            print(nums[mid])
            if nums[mid] > nums[end_idx]:
                bs(mid + 1, end_idx)
            else:
                #no wrap or wrapped is part of 1st seq
                bs(start_idx, mid - 1)
        bs(0, len(nums) - 1)
        return curr