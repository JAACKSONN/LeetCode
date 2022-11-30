class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        
        for target in range(1, n + 1):
            for square in squares:
                if target - square >= 0:
                    dp[target] = min(dp[target], 1 + dp[target - square])
                else:
                    break
        return dp[-1] if dp[-1] != n + 1 else -1