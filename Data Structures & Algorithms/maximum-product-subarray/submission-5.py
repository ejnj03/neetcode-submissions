class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #max neg/pos that includes n - 1 th element
        curr_min = 1
        curr_max = 1
        res = nums[0]
        
        for num in nums:
            cmax, cmin = curr_max * num, curr_min * num
            curr_min = min(cmax, cmin, num)
            curr_max = max(cmax, cmin, num)
            #print(num, curr_min, curr_max)
            res = max(res, curr_max)
        return res