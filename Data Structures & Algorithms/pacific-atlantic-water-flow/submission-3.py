class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nr, nc = len(heights), len(heights[0])
        #q always contains only VALID sqs (that can reach each respective destination)
        po = deque([(0, c) for c in range(1, nc)] + [(r, 0) for r in range(nr)])
        ao = deque([(nr - 1, c - 1) for c in range(nc)] + [(r, nc - 1) for r in range(nr)])
        
        pv, av = set(), set()

        for oc, valid in [(po, pv), (ao, av)]:
            while len(oc) > 0: 
                r, c = oc.popleft()
                valid.add((r, c))
                for nbr, nbc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if nbr < 0 or nbr >= nr or nbc < 0 or nbc >= nc or (nbr, nbc) in valid: continue
                    #skip if cant reach target from nb
                    if heights[r][c] > heights[nbr][nbc]: continue
                    oc.append((nbr, nbc))
        
        return [cell for cell in list(pv.intersection(av))]



                

    
