class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def find(n, l, r): #find insert pos of i
            nonlocal intervals
            sub, inside = None, False
            while l <= r:
                mid = (l + r) // 2
                s, e = intervals[mid]
                if s <= n and n <= e:
                    sub, inside = mid, True
                    break
                if n < s:
                    r = mid - 1
                if n > e:
                    l = mid + 1
            if sub is None: #if it isnt part of an existing range
                sub = r + 1 if r < l else l + 1
            return sub, inside

        #position of start idx 
        start, end = newInterval
        subs, sin = find(start, 0, len(intervals) - 1) #subs := position of the intvl start belongs to
        sube, ein = find(end, subs, len(intervals) - 1)
        l, r = subs, sube
        if sin:
            start = intervals[subs][0]
        if ein:
            end = intervals[sube][1]
            r += 1
        
        return intervals[:l] + [[start, end]] + intervals[r:]
        
        



            