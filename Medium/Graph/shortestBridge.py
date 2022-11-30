class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        count = 0
        
        def isValid(i, j):
            return i >= 0 and i < ROWS and j >= 0 and j < COLS and grid[i][j] != 2
        def dfs(i, j):
            if i >= 0 and i < ROWS and j >= 0 and j < COLS and grid[i][j] == 1:
                q.append((i, j))
                grid[i][j] = 2
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i-1, j)
                dfs(i, j - 1)
        flag = False
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(i, j)
                    flag = True
                    break
            if flag:
                break
        
        
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                if grid[i][j] == 1:
                    return count - 1
                grid[i][j] = 2
                if isValid(i + 1, j): q.append((i + 1, j))
                if isValid(i - 1, j): q.append((i - 1, j))
                if isValid(i, j + 1): q.append((i, j + 1))
                if isValid(i, j - 1): q.append((i, j - 1))
            
            count += 1
        return -1
                    
        
        