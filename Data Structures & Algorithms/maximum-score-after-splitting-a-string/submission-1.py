class Solution:
    def maxScore(self, s: str) -> int:
        score = [1 if int(s[i]) == 0 and i == 0 else 0 for i in range(len(s) - 1)] #count up to 0th idx
        #print([int(si) for si in s])

        for i in range(1, len(s) - 1): #treat i as idx of last 0 
            #print(s[i])
            score[i] = score[i - 1]
            if int(s[i]) == 0:
                score[i] += 1
        
        count = 0

        #print(score)
        for i in range(len(s) - 1, 0, -1): #end non inclusive
            if int(s[i]) == 1:
                count += 1
            score[i - 1] += count
        #print(score)
        return max(score)