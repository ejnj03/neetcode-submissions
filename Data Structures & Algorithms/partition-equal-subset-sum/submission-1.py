class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #get target
        tot = sum(nums)
        target = tot / 2
        if not target.is_integer():
            #unreachable target
            return False
        target = int(target)
        
        
        prev = [(nums[0] if nums[0] <= t else 0) for t in range(target + 1)]
        #iterate over each num
        for last_idx in range(1, len(nums)):
            #not possible if num > target
            num = nums[last_idx] 
            if num > target: return False
            elif num == target: return True

            print(num, nums)
            print(prev)
            curr = []
            for cap in range(target + 1):
                exclude = prev[cap]
                include = 0
                #cant include if > cap
                if num <= cap:
                    include = prev[cap - num] + num
                curr.append(max(include, exclude))
                #reached target
                if curr[cap] == target: return True
            
            prev = curr

        return False 
        