class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        #start at last fence, end at fence 0 
        prev = [[1, 0] for _ in range(k)]
        fence = 1

        while fence < n:
            #sum paths with color used 1 or 2 consec
            used = [sum(paths) for paths in prev]
            tot = sum(used)
            temp = [[0, 0] for _ in range(k)]
            for ci in range(k):
                #all paths exc. prev same color
                temp[ci][0] = tot - used[ci]
                #paths that used same color once
                temp[ci][1] = prev[ci][0]
            prev = temp
            fence+=1
        
        return sum([sum(paths) for paths in prev])

        
        
        