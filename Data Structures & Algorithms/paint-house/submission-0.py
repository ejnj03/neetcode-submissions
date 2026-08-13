class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #prev = 3 columns
        prev = [0, 0, 0]
        house = len(costs) - 1 #i of last row
        
        while house > -1:
            print(prev)
            temp = [0, 0, 0]
            for ci in range(3):
                temp[ci] = costs[house][ci] + min(prev[(ci + 1) % 3], prev[(ci + 2) % 3])
            
            prev = temp
            house -= 1

        return min(prev) #min cost path start position 