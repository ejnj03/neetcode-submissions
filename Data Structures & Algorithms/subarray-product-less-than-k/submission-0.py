class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        lb = 0
        curr = 1
        count = 0 

        for i in range(len(nums)):
            curr *= nums[i]
            while curr >= k and lb < i:
                curr //= nums[lb]
                lb += 1
            #print(curr, nums[lb:i+1])
            if curr < k:
                count += i - lb + 1
            #print(lb, i)
        return count
            