class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        const num_rows = grid.length
        const num_cols = grid[0].length
        const isValid = (r, c) => {
            if (r < 0 || r >= num_rows){
                return false
            }
            if (c < 0 || c >= num_cols) {
                return false
            }
            return true
        }

        const dfs = (crow, ccol) => {
            if (!isValid(crow, ccol) || grid[crow][ccol] == "0") {
                return 0 
            }
            //mark current cell as visited
            grid[crow][ccol] = "0"
            const nbs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

            let island_size = 1
            for (const nb of nbs) {
                const [rinc, cinc] = nb
                island_size += dfs(rinc + crow, cinc + ccol)
            }
            return island_size
        }
        
        let curr_max = 0
        for (let r = 0; r < num_rows; r++) {
            for (let c = 0; c < num_cols; c++) {
                if (grid[r][c] == 1) {
                    const island_size = dfs(r, c)
                    curr_max = Math.max(island_size, curr_max)
                } 
            }
        }
        return curr_max
    }
}
