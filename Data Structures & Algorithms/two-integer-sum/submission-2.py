class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #track every visited num: index
        counter = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in counter:
                return [counter[diff], i]
            #only 1 valid answer exists so can overwrite
            counter[nums[i]] = i
        return []
