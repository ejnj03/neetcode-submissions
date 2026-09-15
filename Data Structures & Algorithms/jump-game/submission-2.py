class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal: #if can reach goal from current position from i, you're able to jump from any position between [i,(i + nums[i])] so check = if goal is in this range 
                goal = i 
        return True if goal == 0 else False