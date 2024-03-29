# https://leetcode.com/problems/surrounded-regions/
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
            
        
        # Top row
        for c in range(COLS):
            if board[0][c] == 'O':
                capture(0, c)
        
        # Bottom row
        if ROWS > 1:
            for c in range(COLS):
                if board[ROWS - 1][c] == 'O':
                    capture(ROWS - 1, c)
        # first col
        for r in range(ROWS):
            if board[r][0] == 'O':
                capture(r, 0)
        # last col
        if COLS > 1:
            for r in range(ROWS):
                if board[r][COLS - 1] == 'O':
                    capture(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
                    
        
            
                    
            

       