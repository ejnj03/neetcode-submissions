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
        seen = {}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            rem = total % k 
            if rem == 0 and i >= 1: return True 
            if rem in seen:
                if total - seen[rem] >= k and i - seen[rem] > 1: #diff is sum of ps[seen + 1: ri]
                    return True
            else:
                seen[rem] = i #lowest idx rem was seen
        
        return False