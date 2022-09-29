class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        dp = [[0 for i in range(COLS + 1)] for j in range(ROWS + 1)]
        result = 0
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, - 1, -1):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
                    result = max(result, dp[r][c])
        return result ** 2