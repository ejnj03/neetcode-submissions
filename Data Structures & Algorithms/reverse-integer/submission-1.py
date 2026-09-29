class Solution:
    def reverse(self, x: int) -> int:
        """
        check for overflow 
        """
        flr, ceil = -(2 ** 31), (2 ** 31) - 1 
        n, res, base = str(x), 0, 1
        sign = 1
        for i in range(len(n)-1, -1, -1):
            try:
                digit = int(n[i])
                if res * 10 + digit > ceil or res * 10 + digit < flr:
                    return 0
                res = res * 10 + digit 
            except:
                sign = -1
        return res * sign
        
            
        