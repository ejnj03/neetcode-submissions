class Solution:
    def reverse(self, x: int) -> int:
        """
        get the lowest digit at each iteration before // 10 on x

        check for overflow BEFORE updating res (should never occur)
        - if res will become greater than ceil on its own after * 10: ret 0 
        - if res will become = to ceil (up to the 10s digit) and digit > 1s digit of ceil: 
        
        *python floor division rounds down towards -1 
            int(n / d) to truncate decimal
        """
        flr, ceil = -(2 ** 31), (2 ** 31) - 1 
        f1, c1 = math.fmod(flr, 10), ceil % 10 #1s digit of the flr and ceil 
        f10, c10 = int(flr / 10), int(ceil / 10) #val excluding the 1s digit divided by 10  
        res = 0
        while x:
            ones = int(math.fmod(x, 10)) #ones digit of current res
            x = int(x / 10) #update x to >> 1 
            #if res * 10 > ceil - ones digit or res * 10 = ceil - ones digit and ones digit of res > ones digit of ceil: 0 
            if (res > c10) or (res == c10 and ones > c1): #above ceil
                return 0 
            if (res < f10) or (res == f10 and ones < f1): #below flr
                return 0
            res = res * 10 + ones 
        return res
        
            
        