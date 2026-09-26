class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        recursive approach on each spiral level 
        """
        rows, cols = len(matrix), len(matrix[0])
        #for row in matrix:
            #print(row)
        #print(rows, cols)
        def border(start, rc, cc, res):
            """
            start: starting index of the spiral (top left idx)
            rc: number of rows in current level
            rn: number of cols in current level
            """
            sr, sc = start
            topr, bottomr, leftc, rightc = sr, sr + rc - 1, sc, sc + cc - 1
            #print(rc, cc)
            if topr > rows - 1 or leftc > cols - 1: return
            if rc < 1 or cc < 1: return
            #dont include last idx of every - iteration
            #top row
            for c in range(leftc, rightc + 1):
                res.append(matrix[topr][c])
            #print(res)
            #left col
            for r in range(topr + 1, bottomr + 1):
                res.append(matrix[r][rightc])
            #print(res)
            if bottomr != topr:
                #bottom row 
                for c in range(rightc - 1, leftc - 1, -1):
                    res.append(matrix[bottomr][c])
            #print(res)
            #right col 
            if rightc != leftc:
                for r in range(bottomr - 1, topr, -1):
                    res.append(matrix[r][leftc])
            #print(res)
            #recurse (even count: round up)
            border((sr + 1, sc + 1), rc - 2, cc - 2, res)
        
        res = []
        border((0, 0), rows, cols, res)
        return res