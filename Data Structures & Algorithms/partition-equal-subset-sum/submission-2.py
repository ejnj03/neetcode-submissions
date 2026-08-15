class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #get target
        tot = sum(nums)
        target = tot / 2
        if not target.is_integer():
            #unreachable target
            return False
        target = int(target)
        
        
        prev = [(True if nums[0] == t or t == 0 else False) for t in range(target + 1)]
        #iterate over each num
        for last_idx in range(1, len(nums)):
            #not possible if num > target
            num = nums[last_idx] 
            if num > target: return False
            elif num == target: return True

            print(num, nums)
            print(prev)
            #0 is always reachable
            curr = [(True if i == 0 else False) for i in range(target + 1)]
            for cap in range(1, target + 1):
                #cap is reachable if cap - num was reachable or cap was reachable
                if num <= cap:
                    curr[cap] = (prev[cap] or prev[cap-num])
            if curr[target] == True: return True
            
            prev = curr

        return False 
        