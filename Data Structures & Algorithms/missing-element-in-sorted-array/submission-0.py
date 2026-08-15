class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        l, r = 0, len(nums) - 1
        start = nums[0]

        while l <= r:
            mid = (l + r) // 2
            #number of missing vals up to this point
            count = nums[mid]- (start + mid)
            print(nums[mid], count)
            if count == k:
                #if gap is here 
                r = mid - 1
                if nums[mid] - nums[mid - 1] > 1:
                    #skipped at different number (lower)
                    break
                #most recently skipped 
            elif count < k: #should check upper interval
                l = mid + 1
            elif count > k: #should check lower interval
                r = mid - 1

        return  nums[r] + (k - (nums[r] - (start + r)))