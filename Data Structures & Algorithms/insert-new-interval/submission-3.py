class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval
        l = len(intervals)
        for i in range(l):
            if intervals[i][0] > end:
                res.append([start, end])
                return res + intervals[i:]
            elif end < intervals[i][1]: #intvls[i][0] <= end < intervals[i][1]
                end = intervals[i][1]
            if intervals[i][1] < start:
                res.append(intervals[i])
            elif intervals[i][0] < start: #intvls[i][0] < start <= intvls[i][end]
                start = intervals[i][0]
            
        res.append([start, end])
        return res
        
        
