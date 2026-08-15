class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        
        pos = [pair for l in lights for pair in [(l[0] - l[1], 1), (l[0] + l[1] + 1, -1)]]  
        pos.sort()
        
        res = [-1, 0] #pos of max, max count
        curr = 0 #curr count
        for pi in range(len(pos)):
            p, inc = pos[pi]
            curr += inc

            res = [p, curr] if curr > res[1] else res

        return res[0]
