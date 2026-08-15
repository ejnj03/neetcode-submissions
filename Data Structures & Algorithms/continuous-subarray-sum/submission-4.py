class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 23 25 29 35 42 
        # 5 1 5 5 0
        # (remr + (k - reml) + n * k = sum in between 
        # want to find remr + (k - reml) = k so same as remr = reml 
        #42 19 17 13 7
        #ps[i] = sum(arr[:i+1])
        #ss[i] = sum(arr[i:]) 
        #k = 6

        # a % k == b % k for b > a if b - a is a factor of k 
        # since for x % k = rem, rem can only be same if x - n * k = rem for any int n  

        ps = [nums[0]]
        for i in range(1, len(nums)):
            ps.append(ps[i - 1] + nums[i])
        
        #print(ps)
        rems = [s % k for s in ps]
        #print(rems)
        seen = {}
        for ri in range(len(rems)):
            rem = rems[ri] 
            if rem == 0 and ri >= 1: return True 
            if rem in seen:
                if ps[ri] - seen[rem] >= k and ri - seen[rem] > 1: #diff is sum of ps[seen + 1: ri]
                    return True
            else:
                seen[rem] = ri #lowest idx rem was seen
        
        return False