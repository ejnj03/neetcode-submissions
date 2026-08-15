class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            print(row)
        numr, numc = len(board), len(board[0])
        
        #iterate over each 3x3 grid -> merge counts after
        rcounts = [{i: 0 for i in range(1, 10)} for _ in range(numr)]
        ccounts = [{i: 0 for i in range(1, 10)} for _ in range(numc)]
        #print(rcounts)
        
        def check_box(rstart, cstart):
            loc = defaultdict(int)

            for r in range(rstart, rstart + 3):
                for c in range(cstart, cstart + 3):
                    val = board[r][c]
                    if val == ".":
                        continue
                    val = int(val)
                    #check locally valid
                    if (loc[val] > 0):
                        return False
                    loc[val] += 1
                    if (rcounts[r][val] > 0 or ccounts[c][val] > 0):
                        return False
                    rcounts[r][val] += 1
                    ccounts[c][val] += 1
            return True

        rpad, rmax = 0, len(board) // 3 
        cmax = len(board[0]) // 3 

        while rpad < rmax:
            cpad = 0
            while cpad < cmax:
                ret = check_box(rpad * 3, cpad * 3)
                if not ret:
                    return False
                cpad += 1
            rpad += 1

        return True
                    
            