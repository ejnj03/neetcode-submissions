class Solution:
    def minWindow(self, s: str, t: str) -> str:

        rem = len(t)
        counter = defaultdict(int)
        for ct in t:
            counter[ct] += 1
        sl, sr, slength = 0, len(s) - 1, float('-inf')
        l=0
        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] -= 1
                if counter[s[r]] >= 0: #if reduced req. count
                    rem -= 1
            while rem <= 0 and l <= r:
                #print(counter, l, r)
                if r - l + 1 <= sr - sl + 1:
                    sl, sr, slength = l, r, r - l + 1
                if s[l] in counter:
                    counter[s[l]] += 1 
                    if counter[s[l]] > 0:
                        rem += 1
                l += 1
        return s[sl:sr+1] if slength > float('-inf') else ""
            
                



            
            