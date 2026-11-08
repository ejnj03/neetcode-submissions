class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        first sort all by position (low to high)
        time = [ time for car i to reach target position ]
        stack - pop car at front 
        fleet's time to end = current fleet time to end

        If two cars start at same position, need to place the faster speed car in front
        or else it will count as the faster car joining the fleet of the slower car 
        ㄴ doesn't matter bc all vals in position are unique 
        """
        t = [(target - p) / s for p, s in sorted(zip(position, speed))]

        res, fleet = 1, t.pop()
        while len(t) > 0:
            curr = t.pop()
            #print(t, curr, fleet, res)
            if curr <= fleet:
                continue #joins current fleet
            else: #curr time to end > fleet time to end
                res += 1
                fleet = curr #new fleet 
            
        
        return res
            