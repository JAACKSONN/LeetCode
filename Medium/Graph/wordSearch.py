class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or word[i] != board[r][c] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            res = (dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
                  )
            
            visited.remove((r,c))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False