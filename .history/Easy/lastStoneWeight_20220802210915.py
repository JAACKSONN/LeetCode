class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            # implies second is larger -5 < -3
            if first < second:
                heapq.heappush(stones, first - second)
                
        stones.append(0)
        return abs(stones[0])