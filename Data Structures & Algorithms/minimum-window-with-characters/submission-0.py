class Solution:
    def minWindow(self, s: str, t: str) -> str:
        curr = {c: 0 for c in t}
        cts = defaultdict(int)
        done = set()
        ret = None
        #desired counts for eaach char
        for c in t:
            cts[c] += 1
        

        st = 0
        en = 0
        while True:
            if en >= len(s):
                break
            enc = s[en]
            if enc in cts:
                curr[enc] += 1
                if curr[enc] == cts[enc]:
                    done.add(enc)

            while st <= en:
                print(f"moving st: {s[st:en+1]}")
                stc = s[st]
                if stc in curr:
                    if curr[stc] > cts[stc]:
                        curr[stc] -= 1
                    else:
                        break
                st += 1

            if len(done) == len(cts.keys()):
                #found all
                if ret is None:
                    ret = s[st:en + 1]
                else:
                    ret = min(ret, s[st:en + 1], key=lambda x: len(x))
            en += 1
        return "" if ret is None else ret