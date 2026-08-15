class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 1 2 4 7 
        #  1 // (2 + 1) + 2/ rolling + new * (i + 1) = 
        nums.sort()
        curr, start = 0, 0 #curr accumulated k
        res = 0 #max count to return 
        for i in range(len(nums) - 1):
            #print(curr, nums[i])
            curr_count = i - start + 1
            update = (nums[i + 1] - nums[i]) * curr_count #add difference
            while update + curr > k:
                curr, start = curr - (nums[i] - nums[start]), start + 1
                curr_count = i - start + 1
                update = (nums[i + 1] - nums[i]) * curr_count #add difference
            
            res = max(res, curr_count)
            curr += update
            #print(curr)
            
        
        return res + 1
            
                

                
        