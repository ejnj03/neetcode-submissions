class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def get_pal(l, r):
            nonlocal count
            start_l = l; start_r = r
            while True:
                #print(s[l:r+1])
                if l < 0 or r >= len(s):
                    break
                if s[l] != s[r]:
                    break
                l -= 1; r += 1
                count += 1

            # from l + 1 up to r - 1
            


        for i in range(len(s)):
            get_pal(i, i)
            if i < len(s) - 1:
                get_pal(i, i+1)
        
        return count