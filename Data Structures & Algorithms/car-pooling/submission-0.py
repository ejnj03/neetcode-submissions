class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    
        #at a given point in time, must only have <= cap passangers
        #ex. 4 from 1 to 2, 3 from 2 to 4
        #ex2. 2 from 1 to 3, 3 from 2 to 4
        #can rep as x = loc, ordered list of (x, delta passangers)
        stops = [st for t in trips for st in [(t[1], t[0]), (t[2], -t[0])]]
        
        stops.sort(key=lambda x:x[0])
        
        count = 0 #current location of bus, current count of passangers on bus 

        for i in range(len(stops)):
            pos, delta = stops[i] #position of bus, change in passangers
            count += delta
            if i == len(stops) - 1 or stops[i + 1][0] != pos: 
                #check valid
                if count > capacity:
                    return False
        
        return True
                 
            
        
            