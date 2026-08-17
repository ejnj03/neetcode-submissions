class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        #ignore first index (0)
        #apply modulo at each step to prevent overflow
        #valid since (C + A * B) % k = ((C % k) + (A % k) * (B % k)) % k 
        memo = [0 if i > 2 else 1 for i in range(numPeople + 1)]
        memo[2] = 1 #1 pair for 2 people
        div = 10**9 + 7
        for n in range(4, numPeople + 1, 2):

            #j: node that has edge to i
            for k in range((n - 2)//2 + 1):
                j = 2 * k + 1
                #left partition
                rp = 2 * k
                lp = n - (2 * k + 2)
                
                memo[n] += memo[rp] * memo[lp] 
                memo[n] %= div
        
        return memo[numPeople]


        