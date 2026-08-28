class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1
        while p1 <= p2:
            #print(re.match(r"[A-Za-z0-9]", s[p2]))
            while not s[p1].isalnum() and p1 < p2:
                p1 += 1
            while not s[p2].isalnum() and p2 > p1:
                p2 -= 1
            s1, s2 = s[p1].lower(), s[p2].lower()
            #print(s1, s2)
            if s1 != s2: return False
            p1, p2 = p1 + 1, p2 - 1
        return True 