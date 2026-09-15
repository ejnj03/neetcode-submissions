class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        sz= len(matrix)

        def rotate(n, offset=0):
            nonlocal matrix 
            for i in range(offset, offset + n - 1): # 0 1 .. [nc - 2] [nc - 1]
                r, c = offset, i
                curr = matrix[r][c]
                for _ in range(4):
                    tr, tc = c, (sz - 1) - r
                    matrix[tr][tc], curr = curr, matrix[tr][tc]
                    r, c = tr, tc
        
        n, offset = sz, 0
        while n > 1:
            rotate(n, offset)
            n -= 2
            offset += 1
        
            

                

        