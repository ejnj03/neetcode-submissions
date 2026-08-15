class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [-1] * k
        self.front = -1
        self.end = -1
        self.filled = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        pos = (self.end + 1) % self.k 
        self.q[pos] = value
        #
        if self.isEmpty():
            self.front = 0
            self.end = 0
        else:
            self.end = pos
        self.filled += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        #clear that position
        self.q[self.front] = -1
        #if this is the last element
        if self.filled == 1:
            self.end = -1
            self.front = -1
        else:
            #the next filled position is
            self.front = (self.front + 1) % self.k
        self.filled -= 1
        return True
            
    def Front(self) -> int:
        return self.q[self.front]

    def Rear(self) -> int:
        return self.q[self.end]
        
    def isEmpty(self) -> bool:
        res = True if self.filled == 0 else False
        return res

    def isFull(self) -> bool:
        #if the front of queue and end of queue are adj or
        #if self.front == 0 and self.end == k - 1:
            #return True
        #elif self.end < self.front and self.front - self.end == 1:
            #return True
        #return False
        res = True if self.filled == self.k else False
        return res


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()