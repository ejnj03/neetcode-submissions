class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        bs for 
        0. no change
            exists (s, e) st s <= new s and new e <= e
        1. no merge + new pair insert
            exists e1 < new s and s2 > new e 
                -> insert (new s, new e) after pair 1
        2. merge 1 (start is in another intvl or end is in another intvl
            exists new e < s2 and (s1, e1) st s1 >= new s and e1 >= new s
                -> update (s1, e1) to (s1, e)
        or  exists new s < e1 and (s2, e2) st s2 >= new e and new e >= e2
                -> update (s2, e2) to (s, e2)
        3. merge 2 
            - (s1, e1) st s1 >= new s and e1 >= new s
            - (s2, e2) st s2 >= new e and new e >= e2

        bs: 
        mid idx = (s + e) // 2 (lower of two idxs if even)
        - if s 
        """

        #bs
        
        def find(n, l, r): #find insert pos of i
            nonlocal intervals
            sub = None
            while l <= r:
                mid = (l + r) // 2
                s, e = intervals[mid]
                if s <= n and n <= e:
                    sub = mid 
                    break
                if n < s:
                    r = mid - 1
                if n > e:
                    l = mid + 1
            if sub is None: #if it isnt part of an existing range
                sub = r + 1 if r < l else l + 1
                #new insert 
                intervals = intervals[:max(0, sub)] + [[n, n]] + intervals[min(sub, len(intervals)):]
            return sub

        #position of start idx 
        start, end = newInterval
        subs = find(start, 0, len(intervals) - 1) #subs := position of the intvl start belongs to
        sube = find(end, subs, len(intervals) - 1)
        return intervals[:max(0, subs)] + [[intervals[subs][0], intervals[sube][1]]] + intervals[min(sube + 1, len(intervals)):]
        
        



            