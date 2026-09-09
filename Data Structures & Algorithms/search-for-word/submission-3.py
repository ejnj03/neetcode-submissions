class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w, h, wlen= len(board[0]), len(board), len(word)

        def check(pos, ci, visited):
            """
            checks if a valid path exists from curr pos that contains substr word[ci:]
            """
            nonlocal wlen
            x, y = pos
            res = False
            #print(x, y)
            if board[y][x] == word[ci]: #curr pos is valid
                if ci == wlen - 1: return True
                nbs = valid(pos, visited) #returns valid nbs
                for nb in nbs:
                    visited.add(nb)
                    res |= check(nb, ci + 1, visited) #check if there is a nb that contains word[ci + 1:]
                    visited.remove(nb)
            return res

        def valid(cpos, visited):
            """
            returns valid nbs of the current position
            """
            nonlocal w, h
            offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            res = []
            px, py = cpos
            for dx, dy in offsets:
                x, y = px + dx, py + dy
                if (x, y) in visited: continue 
                if x <= -1 or x >= w: continue
                if y <= -1 or y >= h: continue
                res.append((x, y))
            return res

        for x in range(w):
            for y in range(h):
                if check((x, y), 0, set([(x, y)])): return True #early stop 
        
        return False
