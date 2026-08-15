class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        l, r = min(sweetness), sum(sweetness)

        while l <= r:
            mid = (l + r)//2
            #print(mid)
            #check if mid sweetness is reachable (everyone at least mid)
            
            curr, rem = 0, k+1 #curr accumulated, remaining ppl

            for i in range(len(sweetness)):
                if rem <= 0: break #early success
                curr += sweetness[i] #update
                if curr >= mid: 
                    rem -= 1 #min filled for a person
                    curr = 0 #reset counter for next person
                #print(rem, curr, sweetness[i])
                
            
            if rem <= 0: 
                #try higher sweetness
                l = mid + 1
            else:
                r = mid - 1
        
        return l - 1