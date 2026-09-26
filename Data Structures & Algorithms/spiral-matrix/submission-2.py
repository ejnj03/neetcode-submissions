class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        based on the optimal solution
        """
        #(dr, dc); right down left up 
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] #even: horizontal move
        nr, nc = len(matrix), len(matrix[0])
        cr, cc, it = 0, -1, 0 #start with dir 0, update to it + 1 % 4 
        steps = [nc, nr - 1] #dir % 2 (0 if col)
        res = []
        while True:
            dr, dc = direction[it % 4]
            num_steps = steps[it % 2]
            if num_steps < 1: break #not dir left and steps <= 1
            for _ in range(num_steps):
                cr, cc = cr + dr, cc + dc
                res.append(matrix[cr][cc])
            steps[it % 2] -= 1
            #print(steps, res)
            it += 1
        
        return res
        