class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        carry = 1
        -> if carry = 0: can return (no more updates needed)
        -> if digit + carry = 10: then carry = 1, digit = 0
        -> else: carry = 0, digit = digit + carry 
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            tot = digits[i] + carry 
            if tot == 10: 
                carry, digits[i] = 1, 0
            else:
                carry, digits[i] = 0, tot
                break #(no more updates needed)
        if carry == 1: #new most significant bit
            digits = [1] + digits
        return digits