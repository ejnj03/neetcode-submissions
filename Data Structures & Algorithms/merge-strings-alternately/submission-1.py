class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = [] #so not init new obj every it (which is the case if s = string)
        curr = 0
        
        while curr < min(len(word1), len(word2)):
            s += word1[curr] + word2[curr]
            curr += 1
        
        s = "".join(s)
        if curr >= len(word1):
            return s + word2[curr:]
        elif curr >= len(word2):
            return s + word1[curr:]
        return "".join(s)