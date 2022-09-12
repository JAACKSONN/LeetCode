class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        deq = collections.deque()
        fresh = 0
        time = 0
        
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    deq.append((r,c))
        
        directions = [[0, 1],[1, 0], [-1, 0], [0, -1]]
    
        while deq and fresh > 0:
            
            for i in range(len(deq)):
                r,c = deq.popleft()
                
                for dx, dy in directions:
                    row = r + dx
                    col = c + dy
                    
                    if row >= 0 and row < ROWS and col >= 0 and col < COLS and grid[row][col] == 1:
                        fresh -= 1
                        deq.append((row, col))
                        grid[row][col] = '2'
            time += 1
        
        return time if fresh == 0 else -1
        
        
                
                
                
        
        
        