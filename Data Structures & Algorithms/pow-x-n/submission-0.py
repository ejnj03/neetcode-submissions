class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1: return x
        if n == 0: return 1
        sign = 1
        if n < 0: 
            sign = -1
            n = sign * n #make positive 
        mid = int(n / 2) #round down
        half = self.myPow(x, mid) #x ^ mid
        res = half * half
        if n % 2 == 1: #is odd 
            res *= x
        return res if sign > 0 else 1/res