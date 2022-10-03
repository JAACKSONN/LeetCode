class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        adj = defaultdict(list)
        
        for i in range(len(routes)):
            for stop in routes[i]:
                adj[stop].append(i)
                
        deq = deque()
        deq.append((source, 0))
        visited = set()
        visited.add(source)
        
        while deq:
            for i in range(len(deq)):
                stop, bus_number = deq.popleft()
                if stop == target:
                    return bus_number
                
                
                for route in adj[stop]:
                    for next_stop in routes[route]:
                        deq.append((next_stop, bus_number + 1))
                        visited.add(next_stop)
                    routes[route] = []
        return -1
                