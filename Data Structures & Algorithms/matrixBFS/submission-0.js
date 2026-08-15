class Solution {
    /**
     * @param {number[][]}
     * @returns {number}
     */
    shortestPath(grid) {
        //immediately return if the dest is invalid 
        const num_rows = grid.length
        const num_cols = grid[0].length
        if (grid[num_rows-1][num_cols-1] == 1) return -1

        console.log(grid)
        const isValid = (row, col) => {
            //check if the psn is valid
            if (Math.min(row, col) < 0 ||row >= num_rows || col >= num_cols) {
                console.log("position invalid: ", row, col)
                return false
            }
            //check if the val at the psn is valid 
            if (grid[row][col] == 1) {
                console.log("Value at position ", row, col, " is invalid: ", grid[row][col])
                return false 
            }
            return true
        }

        const queue = [[0,0]]
        const visited = new Set()
        let curr_dist = 0

        while (queue.length > 0) {
            //iterate over all elements in current distance level 
            let curr_paths = queue.length
            console.log("Current queue length: ", queue.length)
            //iterate over all possible paths at curr level (will break at curr_paths = 0)
            while (curr_paths--) {
                const [row, col] = queue.shift()
                //check if psn is valid
                if (!isValid(row, col)) {
                    console.log("psn is not valid")
                    //dont add its nbs
                    continue
                }
                console.log("Current position: ", row, col)
                //if at dest return current path length
                if (row == num_rows - 1 && col == num_cols - 1) return curr_dist
                //add to visited (bc this is the shortest path to this psn)
                //we dont want the nbs at the current level to visit this psn 
                visited.add(`${row}, ${col}`)
                const nbs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for (const nb of nbs) {
                    const [dr, dc] = nb
                    if (visited.has(`${dr + row}, ${dc + col}`)) {
                        //dont add current position or visited psn
                        continue 
                    }
                    queue.push([row + dr, col + dc])
                }
                
            }
            //all psns in q at this point are curr_dist + 1 away from starting loc
            curr_dist += 1
            console.log("Current distance: ", curr_dist, " Queue state: ")
            console.log(queue, '\n')
            console.log("current visited: ", visited)
        }
        return -1
    }
}
