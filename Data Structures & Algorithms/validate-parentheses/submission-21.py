class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0: return False
        pairs = {'{':'}', '(':')', '[':']'}
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else: #if closing bracket
                if len(stack) == 0 or pairs[stack[-1]] != ch: #most recently opened should be the most recently closed
                    return False 
                stack.pop()
        #true if all opened items have been closed
        return True if len(stack) == 0 else False
            