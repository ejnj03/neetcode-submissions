class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, curr, s = 0, 0, 0
        #ret, curr count of 0s, eoa

        for e in range(len(nums)):
            curr += nums[e] ^ 1
            #print(curr)
            while curr > k:
                #exits when curr >= k or e >= len(nums) - 1
                curr -= nums[s] ^ 1
                s += 1
                #0 if 1, 1 if 0 
            #print(nums[s:e + 1], curr)
            res = max(res, e - s + 1) #e - s + 1 is - or 0 if s > e (no possible config that ends at e)
        
        return res
            
            