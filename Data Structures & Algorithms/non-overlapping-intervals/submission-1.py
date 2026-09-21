class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        """
        1, 11 | 1, 100 | 2, 12 | 11, 12 
        1, 11
        2,
        """
        intervals.sort(key=lambda x: x[0])
        curr, res = None, 0
        for i in intervals:
            start, end = i[0], i[1]
            if curr is not None and start < curr: #new intvl
                if curr > end:
                    curr = end
                res += 1
            else:
                curr = end
           
        return res
