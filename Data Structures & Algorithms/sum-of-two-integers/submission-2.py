class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        carry = 
        """
        carry = 0
        res = a ^ b
        one_mask = 2**32 - 1
        for i in range(32): #up to the 31st bit 
            mask = (1 << i)
            ai, bi = (mask & a) >> i, (mask & b) >> i
            #print(ai, bi, carry, ai + bi + carry)
            if ai + bi + carry == 3:
                res |= mask
                carry = 1
            elif ai + bi + carry == 2:
                res &= (mask ^ one_mask)
                carry = 1
            elif carry == 1:
                res |= mask
                carry = 0
            
        msb = (res >> 31) #check msb for sign

        if msb == 1:
            res = - ((res - 1) ^ one_mask) #flip back to positive 

        return res
