class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26
        offset = ord('a')
        for cs in s:
            chars[ord(cs) - offset] += 1
        for ct in t:
            chars[ord(ct) - offset] -= 1
        
        #print(chars)
        for count in chars:
            if count != 0: return False
        return True