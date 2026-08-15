from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = set()
        rotten_fruits = deque()
        num_rows = len(grid)
        num_cols = len(grid[0])

        #first collect all rotten fruits and all fresh fruits
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    fresh_fruits.add((r, c))
                elif grid[r][c] == 2:
                    rotten_fruits.append((r, c))

        curr_time = 0 # 0 hours elapsed
        #queue state at time t is the fruits that have become rotten at time t-1
        while len(rotten_fruits) > 0:
            #early stop if there are no more fresh fruits left
            if len(fresh_fruits) == 0:
                return curr_time
            for _ in range(len(rotten_fruits)):
                print(curr_time, rotten_fruits)
                r, c = rotten_fruits.popleft()
                nbs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for nb in nbs:
                    dr, dc = nb
                    nb_psn = (r + dr, c + dc)
                    #if fresh fruit remove from fresh fruits so we wont visit again
                    #and add it as a new rotten to the queue
                    if nb_psn in fresh_fruits:
                        fresh_fruits.remove(nb_psn)
                        rotten_fruits.append(nb_psn)
            #visited all that became rotten at curr time
            curr_time += 1
        #if there were no rotten or fresh to begin with
        return -1 if len(fresh_fruits) > 0 else 0
            