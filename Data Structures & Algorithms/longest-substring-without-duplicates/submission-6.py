class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        with seen as map, jump intervals
        """
        if len(s) <= 1:
            return len(s)
        
        res, seen = 1, {s[0]: 0}
        l = 0
        for r in range(1, len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                #jump to the index after char was last seen
                l = seen[s[r]] + 1
            #seq w r is valid now
            seen[s[r]] = r
            res = max(res, r - l + 1)
        
        return res