class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        curr = 0
        
        while True:
            if curr >= len(word1):
                return s + word2[curr:]
            elif curr >= len(word2):
                return s + word1[curr:]
            s += word1[curr] + word2[curr]
            curr += 1
        return s