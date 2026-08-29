class Solution:
    def minWindow(self, s: str, t: str) -> str:

        rem = len(t)
        counter = defaultdict(int)
        for ct in t:
            counter[ct] += 1
        res = ""
        l=0
        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] -= 1
                if counter[s[r]] >= 0: #if reduced req. count
                    rem -= 1
            while rem <= 0 and l <= r:
                #print(counter, l, r)
                if len(res) == 0:
                    res = s[l:r+1]
                res = min(res, s[l:r+1], key=lambda x: len(x))
                if s[l] in counter:
                    counter[s[l]] += 1 
                    if counter[s[l]] > 0:
                        rem += 1
                l += 1
        return res
            
                



            
            