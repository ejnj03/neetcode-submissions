class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        technically you can start at both ends of the array (at house 0 or house n-1)
        and define dp[i][j] to be cost incurred up starting from i up to 0 (if 0 is last house) up to n-1 (if n-1 is last house)
        """
        #prev = 3 columns
        prev = [0, 0, 0]
        house = 0 #i of last row
        
        while house < len(costs):
            temp = [0, 0, 0]
            for ci in range(3):
                temp[ci] = costs[house][ci] + min(prev[(ci + 1) % 3], prev[(ci + 2) % 3])
            
            prev = temp
            house += 1

        return min(prev) #min cost path start position 