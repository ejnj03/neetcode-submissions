class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def ms(l, r):
            if l == r:
                return [intervals[l]]
            mid = (l + r) // 2
            left = ms(l, mid)
            right = ms(mid + 1, r)
            return merge(left, right)
        
        def merge(left, right):
            res = []
            pl, pr = 0, 0

            prev = None
            while pl < len(left) or pr < len(right):
                l, r = left[pl] if pl < len(left) else None, right[pr] if pr < len(right) else None
                if r is None or (l is not None and l[1] < r[0]):
                    update = l
                    pl += 1
                elif l is None or (r is not None and r[1] < l[0]):
                    update = r
                    pr += 1
                else:
                    update = [min(l[0], r[0]), max(l[1], r[1])]
                    pl, pr = pl + 1, pr + 1
                #print("prev: ", prev, " update: ", update)
                if prev is None or prev[1] < update[0]:
                    res.append(update)
                    prev = update
                else:
                    prev = [min(prev[0], update[0]), max(prev[1], update[1])]
                    res[-1] = prev
            #print("res: ", res)
            
            return res
        return ms(0, len(intervals) - 1)
        

        
        