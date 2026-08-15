class TimeMap:

    def __init__(self):
        #store key: vals already in it
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        #print("query: ", timestamp)
        def rec(l, r):
            if l > r: return "", float('inf')
            mid = (l + r)//2
            val, ts = arr[mid]
            #print("current subarr: ", arr[l: r+1])
            #print(f"mid: {arr[mid]}")
            if ts > timestamp:
                res = rec(l, mid - 1)
                return res
                #print(f"returning {res} for subarr", arr[l: r+1])
            elif ts < timestamp:
                ret = rec(mid + 1, r)
                if ret[1] <= timestamp:
                    print(f"returning {ret}")
                    return ret
            #print(f"returning {arr[mid]}")
            return arr[mid]
        
            
        return rec(0, len(arr) - 1)[0]
