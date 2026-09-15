class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, curr = [], 0
        start, end = newInterval
        l = len(intervals)
        while curr < l and intervals[curr][1] < start:
            res.append(intervals[curr])
            curr += 1
        start = min(intervals[curr][0], start) if curr < l else start
        while curr < l and end >= intervals[curr][1]: #exists on curr at pair st end < intvl end
            curr += 1
        if curr < l and end >= intervals[curr][0]:
            end, curr = intervals[curr][1], curr + 1
        res.append([start, end])
        return res + intervals[curr:]
        
