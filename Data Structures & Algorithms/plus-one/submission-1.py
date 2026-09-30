class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        carry = 1
        -> if carry = 0: can return (no more updates needed)
        -> if digit + carry = 10: then carry = 1, digit = 0
        -> else: carry = 0, digit = digit + carry 
        """
        for i in range(len(digits) - 1, -1, -1): #proceeds to next place only when there is carry of 1
            if digits[i] < 9: 
                digits[i] += 1
                return digits
            digits[i] = 0 #means there's carry to next digit

        return [1] + digits