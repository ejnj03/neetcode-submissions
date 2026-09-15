class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval
        l = len(intervals)
        for i in range(l):
            if intervals[i][0] > end:
                res.append([start, end])
                return res + intervals[i:]
            if intervals[i][1] < start:
                res.append(intervals[i])
            else:
                 #intvls[i][0] < start <= intvls[i][end]
                start, end = min(intervals[i][0], start), max(intervals[i][1], end)
            
        res.append([start, end])
        return res
        
        
