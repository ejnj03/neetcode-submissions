class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nc, nr, wl= len(board[0]), len(board), len(word)

        def check(r, c, wi):
            """
            checks if a valid path exists from curr pos that contains substr word[ci:]
            """
            nonlocal wl, nr, nc
            if wi >= wl: return True 
            if r >= nr or r < 0 or c >= nc or c < 0: return False

            char, board[r][c] = board[r][c], "#"

            if char == word[wi]: #curr pos is valid
                offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                for dr, dc in offsets:
                    if check(r + dr, c + dc, wi + 1): return True

            board[r][c] = char
            return False 

        for r in range(nr):
            for c in range(nc):
                if check(r, c, 0): return True #early stop 
        return False
