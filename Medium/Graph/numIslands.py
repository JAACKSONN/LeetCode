class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs (i,j):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                if i + 1 < len(grid): dfs (i + 1, j) 
                if i - 1 >= 0: dfs(i - 1, j)
                if j + 1 < len(grid[0]): dfs(i, j + 1)
                if j - 1 >= 0: dfs(i, j - 1) 
        for  i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs (i, j)
        return count