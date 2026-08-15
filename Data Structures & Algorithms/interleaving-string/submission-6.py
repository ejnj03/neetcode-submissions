class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        curr = [True if (i == 0) else False for i in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            if (s1[i - 1] == s3[i - 1] and curr[i-1] == True):
                curr[i] = True
        print(0, list(["0", *s1]))
        print(0, ["t" if v == True else "f" for v in curr])
        for i2 in range(1, len(s2) + 1):
            c2 = s2[i2 - 1]
            if c2 != s3[i2 - 1] and curr[0] == True:
                curr[0] = False
            for i1 in range(1, len(s1) + 1):
                c1 = s1[i1 - 1]
                i3 = i1 + i2 - 1
                c3 = s3[i3]
                #print("c1: ", c1, " c3: ", c3)
                prev = (curr[i1 - 1] == True or curr[i1] == True)
                if (c1 == c3 and curr[i1 - 1] == True) or (c2 == c3 and curr[i1] == True):
                    curr[i1] = True
                else:
                    curr[i1] = False
                #print(["t" if v == True else "f" for v in curr])
            print(c2, ["t" if v == True else "f" for v in curr])
        return curr[-1]