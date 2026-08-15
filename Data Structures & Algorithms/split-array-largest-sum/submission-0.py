class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        lb, ub = max(nums), sum(nums) #min sum and max sum of subarr

        while lb <= ub:
            
            mid = (lb + ub) // 2 #target min sum 
            #print(mid)
            #print(lb, ub)
            #check if every group can be <= mid
            #want to maximize sum but below threshold
            curr, count = 0, 1
            for i in range(len(nums)):
                if curr + nums[i] > mid:
                    count += 1
                    curr = 0
                curr += nums[i]
                #print(curr, count)
            
            #if it can be split into < k subarrs with sum <= mid, it can be split into k + 1 subarrs with sum <= mid
            if count <= k:
                ub = mid - 1 #try lower sum
            else:
                lb = mid + 1
        
        return ub + 1
                
            
                