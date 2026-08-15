
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #l = -1 # if all elements are > x then l would be 
        #r = len(arr)

        #binary search
        l = 0
        r = len(arr) - 1
        
        #find index l : rightmost element <= x
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                #arr[mid] >= x
                r = mid
        l -= 1
        r = l + 1

        c = 0
        while True:
            l_v = (l > -1 and l < len(arr))
            r_v = (r > -1 and r < len(arr))

            if (not l_v and not r_v) or c == k:
                break

            if not r_v:
                l -= 1 #move left 
            elif not l_v:
                r += 1 #move right
            else:
                s = min(l, r, key=lambda p: abs(arr[p] - x))
                if s == r:
                    r += 1
                else:
                    l -= 1
            c += 1

        return arr[max(l + 1, 0):min(r, len(arr))]