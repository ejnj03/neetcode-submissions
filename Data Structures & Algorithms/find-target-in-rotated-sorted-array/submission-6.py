class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        for any intvl l, r, if n[l] < n[r] that means that that subseq. is sorted (contains vals x : n[l] < x < n[r])
        """
        # 3 4 5 1 2 3 
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target: 
                return mid
            if nums[l] <= nums[mid]: #left side is sorted 
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 #target is in left side
                else:
                    r = mid - 1
            else: #nums[l] > nums[mid] right side is sorted
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

                