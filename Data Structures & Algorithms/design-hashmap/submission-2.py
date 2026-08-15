class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        self.size = 0 #currently filled positions
        self.capacity = 2 #all positions (covers 0, ..., self.capacity - 1)
        self.arr = [None, None]

    def get_pos(self, key):
        #print([(n.key, n.val) if n is not None else ("empty") for n in self.arr])
        #get idx corresponding to node if present, else the first empty idx after it
        curr = key % self.capacity
        while curr < self.capacity: #idx not out of bounds 
            if self.arr[curr] is None or self.arr[curr].key == key:
                break
            curr += 1
        return curr

    def rehash(self):
        self.capacity *= 2
        prev = self.arr
        self.arr = [None] * self.capacity
        for n in prev:
            if n is not None:
                self.put(n.key, n.val)
        
    def put(self, key: int, value: int) -> None:
        curr = self.get_pos(key)
        while curr > self.capacity - 1:
            #rehash then insert
            self.rehash()
            curr = self.get_pos(key)
        if self.arr[curr] is not None: #key alr is in hashmap
            self.arr[curr].val = value
            return
        print(f"inserting {key}, {value} at position {curr}")
        #key is not in hashmap so insert it
        self.arr[curr] = Node(key, value)

    def get(self, key: int) -> int:
        curr = self.get_pos(key)
        if curr < self.capacity and self.arr[curr] is not None:
            return self.arr[curr].val
        return -1

    def remove(self, key: int) -> None:
        curr = self.get_pos(key)
        if curr < self.capacity and self.arr[curr] is not None:
            self.arr[curr] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)