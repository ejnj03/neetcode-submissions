class MedianFinder:

    def __init__(self):
        #max heap of lower vals
        self.l = []
        #min heap of higher vals
        self.r = []

    def move_right(self):
        #moves l max to r
        to_move = heapq.heappop_max(self.l)
        heapq.heappush(self.r, to_move)

    def move_left(self):
        #moves r min to l 
        to_move = heapq.heappop(self.r)
        heapq.heappush_max(self.l, to_move)

    def addNum(self, num: int) -> None:
        #assume max diff of two heaps at this stage is 1
        if len(self.r) > 0 and num > self.r[0]:
            heapq.heappush(self.r, num)
        else:
            heapq.heappush_max(self.l, num)
        
        if len(self.r) - len(self.l) > 1:
            self.move_left()
        if len(self.l) - len(self.r) > 1:
            self.move_right()
        

    def findMedian(self) -> float:
        sl, sr = len(self.l), len(self.r)
        #if both sizes same
        if sl == sr:
            return (self.l[0] + self.r[0]) / 2
        elif sl > sr:
            return self.l[0]
        else:
            return self.r[0]