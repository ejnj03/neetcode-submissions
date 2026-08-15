class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev = [1 for i in range(len(s) + 1)]
        #print(s)
        #print(0, prev)
        #ex. t = "cat"
        for c_t in t:
            #curr: # of subsequences of t[up to c_t] in (cont)
            curr = [0 for _ in range(len(s) + 1)]
            for i_s in range(len(s)):
                # (cont) s[up to c_s]
                c_s = s[i_s] #char is 0 idxed
                i_s = i_s + 1 #grid is 1 idxed
                #number of subseq of t[up to c_t] up to i_s - 1
                curr[i_s] = curr[i_s - 1]

                if c_t == c_s:
                    #if match: add number of subseq ending at i_s to number of subseq ending before it
                    curr[i_s] += prev[i_s - 1]
           #print(c_t, curr)
            prev = curr
        return prev[len(s)]
                
            