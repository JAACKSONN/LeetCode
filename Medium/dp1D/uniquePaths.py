class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // (math.factorial(m - 1) *  math.factorial(n - 1))
        
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         prevRow = [1] * n
        
#         for i in range(m - 1):
#             newRow = [0] * n
#             for j in range(n - 1, -1, -1):
#                 newRow[j] = newRow[j+1] + prevRow[j] if j + 1 < n else prevRow[j]
#             prevRow = newRow
#         return prevRow[0]

            