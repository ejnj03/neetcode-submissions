class Solution:
    def mult(self, n, digit, base=None):
        """
        for n (potentially multi digit), and digit (1 digit) 
        returns prod of n * digit * 10 * (base - 1) (base = 2: 10)
        """
        res, carry = list((base - 1) * [0] if base > 1 else []), 0
        for i in range(len(n) - 1, -1, -1):
            curr = int(digit) * int(n[i]) + carry
            if curr >= 10: 
                carry = curr // 10
            else:
                carry = 0
            res.append(curr % 10)
        if carry:
            res.append(carry)
        return res #returns reversed digits
    
    def add(self, n1, n2):
        """
        add each place
        """
        base, res, carry = 1, [], 0
        for i in range(max(len(n1), len(n2))):
            curr = carry
            if i < len(n1):
                curr += int(n1[i])
            if i < len(n2):
                curr += int(n2[i])
            if curr >= 10: 
                carry = curr // 10
            else:
                carry = 0
            res.append(curr % 10)
        if carry:
            res.append(carry)
        return res

    def multiply(self, num1: str, num2: str) -> str:
        """
        ex. 111, 222
        multiply:
        111 * 2 
        + 111 * 20 
        + ...
        ...
        add
        """
        if num1 == "0" or num2 == "0": return "0"
        base, res = 1, None
        for i in range(len(num2) -1, -1, -1):
            curr = self.mult(num1, num2[i], base)
            #print(curr)
            if not res:
                res = curr
            else:
                res = self.add(res, curr)
                #print(res)
            base += 1
        val = ""
        for i in range(len(res)-1, -1, -1):
            val += str(res[i])
        return val