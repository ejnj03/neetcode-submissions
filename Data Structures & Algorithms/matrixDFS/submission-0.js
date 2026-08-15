class Solution {
    /**
     * @param {number[][]} grid
     * @returns {number}
     */
    countPaths(grid) {
        const num_rows = grid.length
        const num_cols = grid[0].length

        const is_valid = (row, col) => {
            if (row < 0 || row >= num_rows) {
                return false
            }
            if (col < 0 || col >= num_cols) {
                return false
            }
            return true
        }
        
        
        const dfs = (crow, ccol) => {
            if (!is_valid(crow, ccol) || grid[crow][ccol] == 1) {
                return 0
            }
            //is a valid position

            //console.log("curr row and col: ", crow, ccol)
            //console.log("curr visited state: ")
            //for (const row of grid){
                //console.log(row)
            //}

            //if at dest return 1
            if (crow == num_rows - 1 && ccol == num_cols - 1) {
                console.log("reached destination")
                return 1
            }
            
            //mark visited
            grid[crow][ccol] = 1
            //collect all valid paths that pass through current 
            let valid_paths = 0
            const nbs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

            for (const nb of nbs) {
                const [rinc, cinc] = nb
                valid_paths += dfs(rinc + crow, cinc + ccol)
                //console.log("Finished dfs starting at ", rinc + crow, cinc + ccol)
            }
            
            //unmark 
            grid[crow][ccol] = 0
            
            return valid_paths
        }

        return dfs(0, 0)
    }
}
