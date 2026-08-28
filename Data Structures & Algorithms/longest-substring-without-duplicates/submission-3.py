class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        two pointers
        res: longest so far
        seen: chars inside current window
        while r < len(s)
            - if s[r] is in seen:
                current subsequence is the longest substring that starts at l
                seen.remove(s[l])
                l += 1
            - else: update res (max(res, r - l + 1))
                seen.add(s[r])
                r += 1
        return res
        """
        if len(s) <= 1:
            return len(s)
        
        res, seen = 1, set([s[0]])
        l, r = 0, 1
        while r < len(s):
            if s[r] in seen:
                #remove l from window 
                seen.remove(s[l])
                l += 1
            else: #current window is valid 
                seen.add(s[r])
                res = max(res, r - l + 1)
                r += 1
        
        return res