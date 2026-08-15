class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        counter = [0 for _ in range(sum(nums) + 1)]

        res = 0
        curr = 0
        for n in nums:
            curr += n
            
            if curr >= goal:
                #print(counter, curr, curr - goal)
                res += counter[curr - goal]
                if curr - goal == 0:
                    res += 1
            counter[curr] += 1
        

        
        return res