class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ROWS = len(wall)
        count = defaultdict(int)
        for r in range(ROWS):
            index = 0
            for c in range(len(wall[r])):
                val = wall[r][c]
                if index != 0:
                    count[index] += 1
                index += val
        res = 0
        res = max(count.values()) if len(count) >= 1 else 0
        return ROWS - res