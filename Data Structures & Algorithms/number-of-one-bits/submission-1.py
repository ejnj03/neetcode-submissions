class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while True:
            #divide by 2 until reach 0
            if n == 0:
                break
            if n % 2 == 1:
                count += 1
            n = n >> 1
            
        return count