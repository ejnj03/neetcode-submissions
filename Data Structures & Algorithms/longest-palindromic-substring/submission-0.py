class Solution:


    def longestPalindrome(self, s: str) -> str:
        ret = ""
        def get_pal(l, r):
            start_l = l; start_r = r
            while True:
                #print(s[l:r+1])
                if l < 0 or r >= len(s):
                    break
                if s[l] != s[r]:
                    break
                l -= 1; r += 1
            #print(s[l:r+1])
            # from l + 1 up to r - 1
            return s[l + 1:r] 

        for i in range(len(s)):
            ret = max(get_pal(i, i), ret, key= lambda x: len(x))
            if i < len(s) - 1:
                ret = max(get_pal(i, i+1), ret, key= lambda x: len(x))
        
        return ret