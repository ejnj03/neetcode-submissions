class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sz = len(nums)
        #sort
        nums.sort()
        print(nums)
        res = []
        subarr = []
        def find_sums(c, d, sub_target):
            nonlocal res
            
            while c < d:
                print(subarr, nums[c], nums[d])
                curr_sum = nums[c] + nums[d]
                if curr_sum == sub_target:
                    #add the current config to the result
                    res.append(subarr + [nums[c], nums[d]])
                    d -= 1
                    c += 1
                    #print("updated both c and d pointers")
                    #print(subarr, nums[c], nums[d])
                    #increment c until reach unique c
                    while nums[c-1] == nums[c] and c < d:
                        c+=1
                elif curr_sum < sub_target:
                    #increment c
                    c += 1
                else:
                    #curr sum > target so decrement d
                    d -= 1

        #Runtime: every combination of a and b (n * n) * 2 pointer for each combination
        # so (n * n) * n = n^3

        def rec_sum(start, num_elems, sub_target):
            nonlocal subarr
            if num_elems == 2:
                print(subarr)
                find_sums(start, sz - num_elems + 1, sub_target)
                return
            for elem in range(start, sz - num_elems + 1):
                if elem > start and nums[elem] == nums[elem - 1]:
                    continue 
                subarr.append(nums[elem])
                rec_sum(elem + 1, num_elems - 1, sub_target - nums[elem])
                subarr.pop()
        
        rec_sum(0, 4, target)
        return res
        """
        #up to the 4th last element
        for a in range(sz - 3):
            #skip duplicates
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            subarr.append(nums[a])
            #from a + 1 up to the 3rd to last element
            for b in range(a + 1, sz - 2):
                #skip duplicates
                if b > a + 1 and nums[b] == nums[b-1]:
                    continue
                subarr.append(nums[b])
                #c start idx, d start idx
                find_sums(b + 1, sz - 1, target - nums[a] - nums[b])
                subarr.pop()
            subarr.pop()
        """