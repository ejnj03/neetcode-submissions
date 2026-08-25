class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #track every visited num: index
        counter = {}
        for i in range(len(nums)):
            if target - nums[i] in counter:
                return [counter[target - nums[i]], i]
            #only 1 valid answer exists so can overwrite
            counter[nums[i]] = i
        return []
