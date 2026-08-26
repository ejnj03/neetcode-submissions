class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        res[0]: number of strings
        res[1:m+1]: length of each string
        / per entry =>
        net offset = m + 1 indices (0 to index m)
        m+1: start index of first string 
        """
        counts = ""
        data = ""
        for s in strs:
            print(s, len(s))
            counts += str(len(s)) + "/"
            data += s
        total = str(len(data)) + "/"
        return total + counts + data

    def decode(self, s: str) -> List[str]:
        print(s)
        idx = s.find("/")
        total = int(s[:idx]) #total length of string
        concat = s[len(s)-total:] #last {total} elements is the raw string (idx len(s) - total:)
        sizes = s[idx + 1:len(s) - total - 1].split("/")
        print(sizes)
        res = []
        prev = 0

        for size in sizes:
            if size == "": return []
            res.append(concat[prev:prev + int(size)])
            prev += int(size)
        return res