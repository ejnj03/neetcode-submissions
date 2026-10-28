class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        with recursion
        """
        def isValid(l, r):
            #print(s[l], s[r])
            while l < r: 
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        l, r = 0, len(s) - 1
        while l < r: 
            if s[l] != s[r]:
                return isValid(l + 1, r) or isValid(l, r - 1)
            l, r = l + 1, r - 1
        
        return True
