class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        comb = [[1 if text1[i] == text2[j] else 0 for i in range(len(text1))] for j in range(len(text2))]
        visited = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        print(comb)
        num_rows = len(text2)
        num_cols = len(text1)

        def find_match(start_row, start_col):
            if start_row > num_rows - 1 or start_col > num_cols - 1:
                return 0
            if visited[start_row][start_col] == 0:
                comb[start_row][start_col] = max(
                    find_match(start_row, start_col + 1), 
                    find_match(start_row + 1, start_col),
                    comb[start_row][start_col] + find_match(start_row + 1, start_col + 1))
                visited[start_row][start_col] = 1
            return comb[start_row][start_col]
        
        return find_match(0,0)