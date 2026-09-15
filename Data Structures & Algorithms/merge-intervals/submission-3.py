class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        smax = max(interval[0] for interval in intervals)
        mp = [-1] * (smax + 1)
        for s, e in intervals:
            mp[s] = max(mp[s], e)
        
        res, cs = [], None
        for i in range(smax + 1):
            if mp[i] == -1: continue
            if cs is None: 
                cs = i
                continue
            if i > mp[cs]:
                res.append([cs, mp[cs]])
                cs = i
            else: # i <= mp[cs] (in current interval)
                mp[cs] = max(mp[cs], mp[i])
        
        res.append([cs, mp[cs]])
        return res
                

        
        