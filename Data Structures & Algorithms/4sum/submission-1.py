class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sz = len(nums)
        #sort
        nums.sort()
        res = []
        def find_sums(c, d, a, b):
            sub_target = target - (nums[a] + nums[b])
            nonlocal res
            while c < d:
                curr_sum = nums[c] + nums[d]
                if curr_sum == sub_target:
                    #add the current config to the result
                    res.append([nums[a], nums[b], nums[c], nums[d]])
                    d -= 1
                    c += 1
                    #print("updated both c and d pointers")
                    #print([nums[a], nums[b], nums[c], nums[d]])
                    #increment c until reach unique c
                    while nums[c-1] == nums[c] and c < d:
                        c+=1
                elif curr_sum < sub_target:
                    #increment c
                    c += 1
                else:
                    #curr sum > target so decrement d
                    d -= 1

        #up to the 4th last element
        for a in range(sz - 3):
            #skip duplicates
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            #from a + 1 up to the 3rd to last element
            for b in range(a + 1, sz - 2):
                #skip duplicates
                if b > a + 1 and nums[b] == nums[b-1]:
                    continue
                #c start idx, d start idx
                find_sums(b + 1, sz - 1, a, b)
        
        return res