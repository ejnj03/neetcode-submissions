"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.end)
        prev = -1
        for i in intervals:
            if prev > i.start:
                return False
            prev = i.end
        return True
