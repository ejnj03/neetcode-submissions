"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
            """
            we need n rooms when: at a given point (any given) in time theres more than 3 meetings going on 
            strategy: sort by start times 
            keep track of current 
            """
            n = len(intervals)
            starts = sorted([i.start for i in intervals])
            ends = sorted([i.end for i in intervals])
            res, ei = 0, 0
            for si in range(n):
                while starts[si] >= ends[ei]:
                    ei += 1
                res = max(si - ei + 1, res)
            return res
                    
            