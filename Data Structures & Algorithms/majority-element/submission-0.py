class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ca = nums[0]
        c = 1

        for i in range(1, len(nums)):
            if ca == nums[i]:
                c += 1
            else:
                c -= 1
                if c == 0:
                    ca = nums[i]
                    c = 1
        
        return ca