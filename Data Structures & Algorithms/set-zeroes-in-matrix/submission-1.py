class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        """
        iterate over each position in the array
        update each row[i] (init to 1 ) to |= pos in arr
        each col[i] to |= pos in arr
        at the end: update each pos in array based on row[i] or col[i]
        net: visit each position twice (2 * M * N), M + N space for the arrays

        row 0 col 4 row 2 col 5 
        """
        nr, nc = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for r in range(nr):
            for c in range(nc):
                val = matrix[r][c]
                if val == 0:
                    rows.add(r)
                    cols.add(c)
        
        for r in range(nr):
            for c in range(nc):
                if r in rows or c in cols:
                    matrix[r][c] = 0