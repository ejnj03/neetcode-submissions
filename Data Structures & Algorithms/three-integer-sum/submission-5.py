class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ret = []
        prev = None
        for i in range(len(nums) - 2):
            if nums[i] == prev:
                continue
            if nums[i] > 0:
                break
            n = nums[i]
            j = i + 1
            k = len(nums) - 1
            target = -n
           
            while j < k:
                curr = nums[j] + nums[k]
                print(i, j, k, curr)
                if curr == target:
                    ret.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -=1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif curr > target: 
                    k -= 1
                    #decrement k
                else:
                    j += 1
            prev = nums[i]
        return ret