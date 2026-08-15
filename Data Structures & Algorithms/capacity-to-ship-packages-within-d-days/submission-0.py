class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minw = max(weights)
        maxw = sum(weights)
        #bs over the range of possible weights
        def check(cap):
            #print(f"curr cap: {cap}")
            curr_w = 0
            curr_d = 1
            for w in weights:
                #print(f"curr w: {curr_w}, curr_d: {curr_d}")
                if curr_d > days: return False #early return 
                if curr_w + w > cap: 
                    #move onto next day
                    curr_w, curr_d = w, curr_d + 1
                else:
                    curr_w += w #add weight to current day
            if curr_w > cap or curr_d > days: return False #last day cap check
            return True #T if reach eoa without exceeding number of days
        
        while minw <= maxw:
            to_check = (minw + maxw) // 2 #curr median w
            is_valid = check(to_check)
            if is_valid: #curr partition passes
                maxw = to_check - 1
            else: #current partition didnt pass
                minw = to_check + 1 #more lenient 
        # if have like sol = 10 then for 8 9 10 will move l to 10 if 9 doesnt work

        return minw

