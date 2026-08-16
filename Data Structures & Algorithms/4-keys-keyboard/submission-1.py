class Solution:
    def maxA(self, n: int) -> int:
        """
        f(i): max As up to i
        block(m): m sized sequence consisting of ctrl-A - ctrl-C - (m - 2) ctrl-Vs 
        i+1 can be 
        1. another A
        2. start of a block
        3. inside a block started from before i + 1

        """

        f = [i for i in range(n + 1)]

        for i in range(3, n - 2):
            #cases where i is the start of a block that ends at j
            #beyond j = 5, starting another block yields >= outcome 
            for j in range(i + 2, min(n, i + 6) + 1):
                f[j] = max((j - (i + 2) + 1) * f[i], f[j])
        
        return f[-1]
                
        

        