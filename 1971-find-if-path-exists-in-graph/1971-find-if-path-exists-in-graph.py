from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visted = set()

        def dfs(node, visted):
            if node == destination:
                return True
            visted.add(node)

            for neigh in graph[node]:
                if neigh not in visted:
                    if dfs(neigh,visted):
                        return True
            return False

        return dfs(source,visted)

