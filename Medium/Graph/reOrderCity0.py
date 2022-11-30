class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        edges = { (a,b) for a,b in connections}
        neighbors = {a : [] for a in range(n)}
        count = 0
        
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
            
        def dfs(node):
            nonlocal count, visited
            if node in visited:
                return
            visited.add(node)
            for neighbor in neighbors[node]:
                if neighbor in visited:
                    continue
                if (node, neighbor) in edges:
                    count += 1
                dfs(neighbor)
        dfs(0)
        return count
                