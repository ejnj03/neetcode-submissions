class Solution:
    def reverse(self, x: int) -> int:
        """
        convert number to string, += on each digit
        if >= 2^31 then pass
        """
        n, res, base = str(x), 0, 1
        sign = 1
        for i in range(len(n)):
            try:
                res += int(n[i]) * base
                if res >= 2**31 - 1: return 0 
                base *= 10 
            except:
                sign = -1
        return res * sign
        
            
        