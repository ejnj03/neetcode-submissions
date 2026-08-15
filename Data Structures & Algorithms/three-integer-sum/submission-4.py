class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ret = set()
        prev = None
        for i in range(len(nums) - 2):
            
            if nums[i] == prev:
                continue
            n = nums[i]
            j = i + 1
            k = len(nums) - 1
            target = -n
           
            while True:
                if j >= k:
                    break
                curr = nums[j] + nums[k]
                print(i, j, k, curr)
                if curr == target:
                    ret.add((nums[i], nums[j], nums[k]))
                    #break
                    j += 1
                    k -=1
                elif curr > target: 
                    while True:
                        k -= 1
                        #print(k)
                        if nums[k+1] != nums[k] or k == j:
                             break
                    #decrement k
                else:
                    while True:
                        print(j)
                        j += 1
                        if nums[j-1] != nums[j] or j == k:
                             break
                    #increment j 
            prev = nums[i]
        return list(ret)