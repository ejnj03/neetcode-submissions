class NumMatrix {
    /**
     * @param {number[][]} matrix
     */
    constructor(matrix) {
        console.log(matrix)
        //reference
        this.matrix = matrix;
        for (let r = 0; r < matrix.length; r++) {
            for (let c = 0; c < matrix[0].length; c++) {
                //same col row above
                const upper_val = r == 0 ? 0 : matrix[r-1][c]
                //same row col before
                const left_val = c == 0 ? 0 : matrix[r][c-1]
                //corner val is 0 if either is 0
                const corner_val = (r == 0 || c == 0) ? 0 : matrix[r-1][c-1]

                //val at this entry is val at this entry + left + up - corner
                matrix[r][c] = matrix[r][c] + upper_val + left_val - corner_val;
            }
        }
        console.log(matrix)
    }

    /**
     * @param {number} row1
     * @param {number} col1
     * @param {number} row2
     * @param {number} col2
     * @return {number}
     */
    sumRegion(row1, col1, row2, col2) {
        let matrix = this.matrix;
        const upper_val = row1 == 0 ? 0 : matrix[row1-1][col2]
        //same row col before
        const left_val = col1 == 0 ? 0 : matrix[row2][col1-1]
        //corner val is 0 if either is 0
        const corner_val = (row1 == 0 || col1 == 0) ? 0 : matrix[row1-1][col1-1]
        return matrix[row2][col2] - upper_val - left_val + corner_val;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
