class Solution:
    def numDecodings(self, s: str) -> int:
        #init to 1 (assume that :0 is 1 possible combination)
        counts = [1, 1, 1] #keep track of i, i - 1, i - 2
        digits = [0, 0, 0]
        for i in range(len(s)):
            digit = int(s[i])
            #valid combinations of ... [i - 1] [i] and ... [i]
            one = counts[(i - 1) % 3] if digit > 0 else 0
            # valid two digits are 1 (0-9) or 2 (0-6)
            two = counts[(i - 2) % 3] if (digits[(i - 1) % 3] == 2 and digit <= 6) or digits[(i - 1) % 3] == 1 else 0
            digits[i % 3], counts[i % 3] = digit, one + two
        return counts[(len(s) - 1) % 3]

            