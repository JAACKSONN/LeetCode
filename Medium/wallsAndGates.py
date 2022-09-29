class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        deq = collections.deque()
        dist = 1 
        ROWS, COLS = len(rooms), len(rooms[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    deq.append((r,c))
        
        directions = [[0,1], [1,0], [-1, 0], [0, -1]]
        while deq:
            for i in range(len(deq)):
                r, c = deq.popleft()
                
                for dx, dy in directions:
                    row = r + dx
                    col = c + dy
                    
                    if row >= 0 and row < ROWS and col >= 0 and col < COLS and rooms[row][col] == 2147483647:
                        rooms[row][col] = dist
                        deq.append((row,col))
            dist += 1
        return rooms
                
        