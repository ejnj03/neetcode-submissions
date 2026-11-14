class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        iterate over all cells
            if cell is O and on border -> run dfs to get its connected cells (stay O)
        """
        def get_nbs(row, col, visited):
            nbs = []
            if row > 0:
                nbs.append((row - 1, col)) #up
            if row < rs - 1:
                nbs.append((row + 1, col)) #down 
            if col > 0:
                nbs.append((row, col - 1)) #left
            if col < cs - 1: 
                nbs.append((row, col + 1))
            return [(r, c) for r, c in nbs if (r, c) not in visited and board[r][c] == "O"]

        rs, cs = len(board), len(board[0])
        stay = []
        
        def dfs(r, c):
            visited = set()
            curr = [(r, c)]
            while len(curr) > 0:
                r, c = curr.pop()
                visited.add((r, c))
                nbs = get_nbs(r, c, visited)
                curr.extend(nbs)
                visited.update(nbs)
            return visited
            
        #run on borders
        keep = set()
        for r in [0, rs - 1]:
            for c in range(cs):
                if board[r][c] == "O" and (r, c) not in keep:
                    keep.update(dfs(r, c))

        for c in [0, cs - 1]:
            for r in range(rs):
                if board[r][c] == "O" and (r, c) not in keep:
                    keep.update(dfs(r, c))
        
        for r in range(rs):
            for c in range(cs):
                if board[r][c] == "O" and (r, c) not in keep:
                    board[r][c] = "X"

