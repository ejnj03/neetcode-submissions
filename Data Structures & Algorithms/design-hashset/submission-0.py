class MyHashSet:

    def __init__(self):
        key_max = 10**6 #max int val of key [0, key_max]
        #means that we need 10**6 + 1 bits for full representation = num ints 
        bit_range = 10**6 + 1
        num_idxs = math.ceil(bit_range / 32) #int is 4 bytes so each position covers 32 bits
        self.arr = [0 for _ in range(num_idxs)]

    def convert(self, key: int):
        #get arr pos, bit pos
        arr_pos = key // 32 ##round down to nearest int
        key_pos = key % 32
        return arr_pos, key_pos  

    def add(self, key: int) -> None:
        aidx, bidx = self.convert(key)
        self.arr[aidx] = self.arr[aidx] | 1 << bidx

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        aidx, bidx = self.convert(key)
        bit_mask = ~(1 << bidx)
        self.arr[aidx] = self.arr[aidx] & bit_mask

    def contains(self, key: int) -> bool:
        aidx, bidx = self.convert(key)
        bit_mask = 1 << bidx
        return bool((self.arr[aidx] & bit_mask) >> bidx)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)