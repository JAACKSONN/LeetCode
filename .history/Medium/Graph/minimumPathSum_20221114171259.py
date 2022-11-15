class Solution:
    def minPathSum(self, grid):
        M, N = len(grid), len(grid[0])
        for i in range(M -1, -1, -1):
            for j in range(N - 1, -1, -1):
                if(i == M - 1 and j != N - 1):
                    grid[i][j] = grid[i][j] +  grid[i][j + 1]
                elif(j == N - 1 and i != M - 1):
                    grid[i][j] = grid[i][j] + grid[i + 1][j]
                elif(j != N - 1 and i != M - 1):
                    grid[i][j] = grid[i][j] + min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]
    # def minPathSum(self, grid):
    #     M, N = len(grid), len(grid[0])
    #     dp = [[0] * N for _ in range(M)]
    #     for i in range(M -1, -1, -1):
    #         for j in range(N - 1, -1, -1):
    #             if(i == M - 1 and j != N - 1):
    #                 dp[i][j] = grid[i][j] +  dp[i][j + 1]
    #             elif(j == N - 1 and i != M - 1):
    #                 dp[i][j] = grid[i][j] + dp[i + 1][j]
    #             elif(j != N - 1 and i != M - 1):
    #                 dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
    #             else:
    #                 dp[i][j] = grid[i][j]
    #     return dp[0][0]