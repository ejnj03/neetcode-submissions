class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        if len(s) % 2 != 0: return False
        pairs = {'{':'}', '(':')', '[':']'}
        for ch in s:
            if ch in pairs:
                q.append(ch)
            else: #if closing bracket
                if len(q) == 0 or pairs[q[-1]] != ch: #most recently opened should be the most recently closed
                    return False 
                q.pop()
        #true if all opened items have been closed
        return True if len(q) == 0 else False
            