class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def twoSum(tidx, l, r):
            nonlocal res, nums
            target = -nums[tidx]
            #print(target)
            while l < r: #two can't be same indices
                val = nums[l] + nums[r]
                if val < target:
                    l += 1 #make more positive
                elif val > target:
                    r -= 1 #make value smaller
                else:
                    res.append([nums[tidx], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1

        prev = None
        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            twoSum(i, i + 1, len(nums) - 1)
            prev = nums[i]
            
        return res
                