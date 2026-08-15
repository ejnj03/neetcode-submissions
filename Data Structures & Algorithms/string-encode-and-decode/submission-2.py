class Solution:

    def encode(self, strs: List[str]) -> str:
        #return "[end]".join(strs)
        lens = ""
        for s in strs:
            lens += f"{str(len(s))},"
        return lens + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        sizes = []
        start = -1
        curr_size = ""

        for i in range(len(s)):
            c = s[i]
            if c == "#":
                start = i + 1
                break
            if c != ",":
                curr_size += c
            else:
                sizes.append(int(curr_size))
                curr_size = ""
        
        ret = []
        for size in sizes:
            ret.append(s[start:start + size])
            start += size
        return ret 
                
