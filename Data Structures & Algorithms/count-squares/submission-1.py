class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
class CountSquares:
    """
    valid square that includes point (x, y)
    - p1 shares same x coord (dist from (x, y): y - p1y)
    - p2 shares same y coord (dist from (x, y): x - p2x)
    - (p2x, p1y)
    """

    def __init__(self):
        self.pointx = defaultdict(lambda: defaultdict(int))   
        self.pointy = defaultdict(lambda: defaultdict(int))    
        
    def add(self, point: List[int]) -> None:
        x, y = point 
        self.pointx[x][y] += 1
        self.pointy[y][x] += 1

    def count(self, point: List[int]) -> int:
        x, y = point 
        xs = self.pointx[x] #same x coord
        ys = self.pointy[y] #same y coord
        #print(x, y, xs, ys)
        tot = 0
        for p1y, count1 in xs.items(): #(x, y +- dist1)
            if p1y == y: continue
            dist1 = abs(y - p1y)
            cands = [x + dist1, x - dist1]
            for cand in cands: 
                if cand in ys: #check if there is (x +/- dist , y) with same dist
                    count2 = ys[cand]
                    if cand in self.pointx and p1y in self.pointx[cand]:  #check if theres (x + dist, p1y)
                        tot += self.pointx[cand][p1y] * count2 * count1
        
        return tot

                    
                
        
