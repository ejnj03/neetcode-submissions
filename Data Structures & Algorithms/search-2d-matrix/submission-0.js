class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        //determine which row first
        const row_idx = this.find_row(matrix, target);
        if (row_idx == null) {
            return false;
        }
        //search within the row

        const row = matrix[row_idx]
        let l = 0;
        let r = row.length - 1;
        while(l <= r) {
            const pivot_idx = Math.floor((r-l+1)/2) + l;
            const pivot_val = row[pivot_idx];
            if (target < pivot_val) {
                r = pivot_idx - 1;
            } else if (target > pivot_val) {
                l = pivot_idx + 1;
            } else {
                //pivot val = target
                //return pivot_idx
                return true;
            }
        }
        return false;
    }

    find_row(matrix, target) {
        let top = 0;
        let bottom = matrix.length - 1;
        let num_cols = matrix[0].length
        while(top <= bottom) {
            //current subarr pivot rows idx
            const pivot_idx = Math.floor((bottom - top + 1)/2) + top
            //console.log(matrix[pivot_idx], " pivot idx: ", pivot_idx)
            const pivot_val = matrix[pivot_idx][0]
            if (target < pivot_val) {
                //top idx up to before pivot idx
                bottom = pivot_idx - 1;
            } else if (target >= pivot_val && target <= matrix[pivot_idx][num_cols-1]) {
                //in the current pivot row
                //console.log("returning row: ", pivot_idx)
                return pivot_idx;
            } else {
                //target > pivot row range
                top = pivot_idx + 1;
            }
        }
        //target cannot be in the matrix
        return null;
    }
}
