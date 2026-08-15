class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    
        #at a given point in time, must only have <= cap passangers
        #ex. 4 from 1 to 2, 3 from 2 to 4
        #ex2. 2 from 1 to 3, 3 from 2 to 4
        #can rep as x = loc, ordered list of (x, delta passangers)
        
        #find the min pos and max pos
        #to minimize space (for large delta st, end // sparse array - sort by [1] and sort by [2], create lists of each)
        st = min(trips, key=lambda t: t[1])[1] #first pickup loc
        end = max(trips, key=lambda t: t[2])[2] #last dropoff loc

        stops = [0 for _ in range(0, end - st + 1)]

        for delta, on, off in trips:
            stops[on - st] += delta
            stops[off - st] -= delta

        curr = 0
        for stop in stops:
            curr += stop
            if curr > capacity:
                return False
        
        return True
            
        
            