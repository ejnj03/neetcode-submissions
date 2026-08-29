class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        def rec(l, r):
            nonlocal nums
            #print(nums[l], nums[r])
            if nums[l] <= nums[r] or r == l: #current array is sorted
                return nums[l] 
            mid = (r + l) // 2
            if nums[l] > nums[mid]:
                return rec(l, mid)
            else:
                return rec(mid + 1, r)
        
        return rec(0, len(nums) - 1)
            
            
        