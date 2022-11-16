class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not n:
            return True

        adj = {i : [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(label, prev):

            if label in visited:
                return False
            
            visited.add(label)

            for nei in adj[label]:
                if nei == prev:
                    continue
                if not dfs(nei, label):
                    return False
            return True 
        
        return dfs(0, -1) and len(visited) == n