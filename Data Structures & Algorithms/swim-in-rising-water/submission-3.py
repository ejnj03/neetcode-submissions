from pprint import pprint
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #min time possible = the value at the bottom right square
        print("start")
        heap = [(grid[0][0], (0,0))]
        incs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        grid_rows = len(grid)
        grid_cols = len(grid[0])

        def isValid(psn):
            x, y = psn
            if min(x, y) > -1 and x < grid_rows and y < grid_cols:
                return True
            return False
        #if we've popped it from the queue, its visited
        visited = set()
        print(heap)
        while True:
            print(f"Heap: {heap}")
            pprint(grid)
            t, psn = heapq.heappop(heap)
            if (psn == (grid_rows-1, grid_cols-1)):
                return t
            x, y = psn
            #mark psn as visited
            visited.add(psn)
            #add nbs
            for inc in incs:
                dx, dy = inc
                nb = (x + dx, y + dy)
                #print(f"nb: {nb}")
                #havent found the shortest dist to it yet
                if nb not in visited and isValid(nb):
                    nb_t = max(t, grid[x + dx][y + dy])
                    if ((nb_t), nb) not in heap:
                        heapq.heappush(heap, (nb_t, nb))
        
            
            
            