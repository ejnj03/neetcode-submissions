class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        """
        res = 1
        counter= defaultdict(int)
        l = 0
        curr = s[l]
        for r in range(len(s)):
            counter[s[r]] += 1
            curr = max([curr, s[r]], key= lambda x: counter[x])
            while (r - l + 1) - counter[curr] > k:
                counter[s[l]] -= 1
                l += 1
                curr = max([curr, s[l]], key= lambda x: counter[x])
            #print(counter)
            #print(l, r)
            res = max(res, min(len(s), counter[curr] + k))
        return res