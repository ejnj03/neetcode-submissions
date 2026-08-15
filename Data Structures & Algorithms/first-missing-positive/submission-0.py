class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            #if X need to consider
            if nums[i] < 1 or nums[i] > len(nums):
                i += 1
                continue
            #if already marked (val is at idx val - 1)
            if nums[nums[i] - 1] == nums[i]:
                i += 1
                continue
            #mark the index (nums[i] - 1) corresponding to the number visited
            #by swapping
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        print(nums)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return len(nums) + 1
