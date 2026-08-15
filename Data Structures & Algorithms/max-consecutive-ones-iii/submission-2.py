class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, curr, s = 0, 0, 0
        #ret, curr count of 0s, eoa

        for e in range(len(nums)):
            curr += nums[e] ^ 1
            #print(curr)
            while curr > k and s < e:
                #exits when curr >= k or e >= len(nums) - 1
                curr -= nums[s] ^ 1
                s += 1
                #0 if 1, 1 if 0 
            #print(nums[s:e + 1], curr)
            if curr <= k:
                res = max(res, e - s + 1)
        
        return res
            
            