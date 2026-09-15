class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        initialize hashmap of str length : list(words)
        for each pos i in s: 
            if curr pos - shortest + 1 < 0: skip this pos
            curr substr init: s[pos-shortest + 1:i]
            iterate over offsets (0, longest - shortest):
            
        """
        #keep track of all ending indices of previous complete words 
        #each step: compute offset from that work
        wlens = defaultdict(list)
        for w in wordDict:
            wlens[len(w)].append(w)

        ls = list(wlens.keys())
        ls.sort() #sorted word lengths
        starts = [0] * (len(s) + 1)
        starts[0] = 1 #is a valid starting position (i - 1 = end of word)
        
        for ci in range(ls[0] - 1, len(s)):
            for wl in ls:
                if ci - wl + 1 < 0 or starts[ci + 1] == 1: continue
                if starts[ci - wl + 1] == 1 and s[ci - wl + 1:ci + 1] in wlens[wl]:
                    starts[ci + 1] = 1
        return True if starts[-1] == 1 else False

            
        