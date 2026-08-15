
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = -1 # if all elements are > x then l would be 
        r = len(arr)
        #l_r = []
        #r_r = []
        for i in range(len(arr)):
            #first idx thats greater than x
            if arr[i] > x:
                r = i
                break
            #last idx thats <= x
            elif arr[i] <= x:
                l = i
            #put r ptr at the first element that greater than x
        
        c = 0
        while True:
            l_v = (l > -1 and l < len(arr))
            #print(f"left idx: {l} value: {arr[l]} valid: {l_v}")
            r_v = (r > -1 and r < len(arr))
            #print(f"right idx: {r} value: {arr[r]} valid: {r_v}")
            #if (not l_v and not r_v) or (len(l_r) + len(r_r) == k):
            print(c)
            if (not l_v and not r_v) or c == k:
                print(l, r)
                break
            if not r_v:
                print(f"left idx: {l} value: {arr[l]} valid: {l_v}")
                #l_r.append(arr[l])
                l -= 1 #move left 
            elif not l_v:
                print(f"right idx: {r} value: {arr[r]} valid: {r_v}")
                #r_r.append(arr[r])
                r += 1 #move right
            else:
                print(f"right idx: {r} value: {arr[r]} valid: {r_v}")
                #both locations are valid
                #if dist is same will choose left 
                s = min(l, r, key=lambda p: abs(arr[p] - x))
                if s == r:
                    print(f"right idx: {r} value: {arr[r]} valid: {r_v}")
                    #r_r.append(arr[r])
                    r += 1
                else:
                    print(f"left idx: {l} value: {arr[l]} valid: {l_v}")
                    #l_r.append(arr[l])
                    l -= 1
            c += 1
        #r_r.reverse()
        #l_r.reverse()
        #l_r.extend(r_r)
        #return l_r
        return arr[max(l + 1, 0):min(r, len(arr))]