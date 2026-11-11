class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        #last idx of previous subset added
        
        def isPalindrome(l, r):
            nonlocal s
            while l <= r:
                if s[l] != s[r]:
                    return False 
                l, r = l + 1, r - 1
            return True 
            
        def split(prev, i):
            nonlocal res, curr, s
            if prev == len(s) - 1:
                res.append(curr.copy())
                return
            if i > len(s) - 1: return
            #print(f"current substring: {s[prev + 1: i + 1]}")
            #print(f"is palindrome: {isPalindrome(prev + 1, i)}")
            #print(f"current curr: {curr}")
            if isPalindrome(prev + 1, i):
                curr.append(s[prev + 1: i + 1])
                #print(f"current curr: {curr} {i}")
                split(i, i + 1)
                curr.pop()
            split(prev, i + 1) #don't parition at current index

        split(-1, 0)
        return res