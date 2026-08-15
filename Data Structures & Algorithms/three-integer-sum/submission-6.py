class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ret = []
        prev = None
        for i, a in enumerate(nums):
            if a == prev:
                continue
            if nums[i] > 0:
                break
            n = nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr = nums[j] + nums[k] + a
                print(i, j, k, curr)
                if curr == 0:
                    ret.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -=1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif curr > 0: 
                    k -= 1
                    #decrement k
                else:
                    j += 1
            prev = a
        return ret