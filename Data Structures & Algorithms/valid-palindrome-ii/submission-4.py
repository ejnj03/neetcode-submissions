class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        with recursion
        """
        def isValid(l, r, deleted):
            #print(s[l], s[r])
            if l >= r: return True #done
            if s[l] == s[r]:
                return isValid(l + 1, r - 1, deleted)
            if deleted: return False

            res = False
            if s[l + 1] == s[r]:
                res |= isValid(l + 2, r - 1, True)
            if s[l] == s[r - 1]:
                res |= isValid(l + 1, r - 2, True)
            return res

        return isValid(0, len(s) - 1, False)