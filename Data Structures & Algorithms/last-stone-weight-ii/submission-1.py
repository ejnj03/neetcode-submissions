class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #get target
        tot = sum(stones)
        print(tot)
        target = tot / 2
        target = math.ceil(target)
        print("target: ", target)
        rem = tot - target
        
        prev = [(True if stones[0] == t or t == 0 else False) for t in range(target + 1)]
        #iterate over each num
        for last_idx in range(1, len(stones)):
            #not possible if num > target
            num = stones[last_idx] 
            if num >= target: return tot - num

            print(num, stones)
            print(prev)
            #0 is always reachable
            curr = [(True if i == 0 else False) for i in range(target + 1)]
            for cap in range(1, target + 1):
                #cap is reachable if cap - num was reachable or cap was reachable
                inc = False 
                if num <= cap:
                    inc = prev[cap-num]
                curr[cap] = (inc or prev[cap])
            if curr[target] == True: return target - rem
            
            prev = curr
            
        reachable = [i for i in range(target + 1) if prev[i] == True]
        print("reachable max: ",  max(reachable))
        return abs(max(reachable) - (tot - max(reachable))) 