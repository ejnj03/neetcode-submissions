class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pprod, sprod = nums.copy(), nums.copy()
        for i in range(1, len(nums)):
            pprod[i] *= pprod[i - 1]
            sprod[len(nums) - 1 - i] *= sprod[len(nums) - i]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                pref = 1
            else:
                pref = pprod[i - 1]
            if i == len(nums) - 1:
                suff = 1
            else:
                suff = sprod[i + 1]
            res.append(pref * suff)
        return res
            
        