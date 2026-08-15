class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #use word 1 to get to word 2
        prev = [i for i in range(len(word1) + 1)]
        print(0, "   ", "  ".join(list(word1)))
        print(0, prev)
        #iterate over rows (chars in word 2)
        #number of ops for w1[:x] to get to w2[:y]
        for i_2 in range(1, len(word2) + 1):
            curr = [i_2 if i == 0 else 0 for i in range(len(word1) + 1)]
            c_2 = word2[i_2 - 1] #0 idxd
            for i_1 in range(1, len(word1) + 1):
                c_1 = word1[i_1 - 1] #0 idxd
                if c_1 == c_2:
                    curr[i_1] = prev[i_1 - 1] #min ops up to match char
                else:
                    # match :i_1- 1 to :i_2 and remove i_1
                    # or match :i_1 to :i_2 - 1 and add i_2
                    #if matched up to i_1 - 1, i_2 -1, replace i_1 with i_2
                    curr[i_1] = min(1 + min(curr[i_1 - 1], prev[i_1]), prev[i_1-1] + 1)
            print(c_2, curr)
            prev = curr

        return prev[-1]
                