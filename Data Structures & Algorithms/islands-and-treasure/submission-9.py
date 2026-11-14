

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        BFS to find solution that reaches a 0 cell first
        """
        rs, cs = len(grid), len(grid[0])
        inf = 2**31 - 1
        
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
            return [(r, c) for r, c in nbs if grid[r][c] > 0 and (r, c) not in visited] 

        def bfs(treasure_cells):
            visited = set()
            curr, ncells, dist = deque(treasure_cells), deque([]), 0
            while True:
                #print(f"\n cell: {r} {c}")
                if len(curr) == 0:
                    if len(ncells) == 0: return
                    curr, ncells, dist = ncells, deque([]), dist + 1
                r, c = curr.popleft()
                grid[r][c] = dist
                nbs = get_nbs(r, c, visited)
                visited.update(nbs)
                ncells.extend(nbs)
        
        cells = []
        for r in range(rs):
            for c in range(cs):
                if grid[r][c] == 0:
                    cells.append((r, c))
        
        bfs(cells)
        
