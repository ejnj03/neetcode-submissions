class Solution:
    #top down approach
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def F(i, inc): #i, includes 0th element
            if i >= len(nums) - 1:
                #can't include last if includes first 
                if i > len(nums) - 1 or inc: return 0
                return nums[i]
            if (i, inc) in memo: return memo[(i, inc)]

            res = max(nums[i] + F(i + 2, inc), 0 + F(i + 1, inc))
            memo[(i, inc)] = res
            #print(memo)
            return res
            
        return max(F(1, False), F(2, False), nums[0] + F(2, True))