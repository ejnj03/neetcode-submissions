class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        #sort 
        nums.sort()
        l, r = 0, nums[len(nums) - 1] - nums[0] #max and min difference
        
        while l <= r:
            mid = (l + r) // 2 #diff to check
            #check over array
            pairs, curr = 0, 0 
            while curr < len(nums) - 1:
                if pairs >= p: break #found target # of valid pairs 
                if nums[curr + 1] - nums[curr] <= mid: #if diff is valid
                    pairs += 1
                    curr += 1 #skip the pair
                curr += 1 #can skip current idx since its min diff w any element in the array > mid
            if pairs < p: #inc target diff 
                l = mid + 1
            else:
                r = mid - 1
            #print(mid, l, r)
        return r + 1 # r will be moved to a valid pos - 1
            
            