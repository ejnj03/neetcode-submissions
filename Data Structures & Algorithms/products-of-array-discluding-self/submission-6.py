class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(1) solution
        res = [1] * len(nums)
        pref = nums[0]
        for i in range(1, len(nums)):
            #res[i - 1] is the pref sum excluding nums[i - 1]
            res[i] *= pref
            pref *= nums[i]
        
        suff = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= suff #multiply by [i + 1:]
            suff *= nums[i] #
        
        return res
        
        
