from collections import defaultdict

class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        min_degree = float('inf')
        degree = defaultdict(int)
        for u in range(1, n+1):
            degree[u] = len(graph[u])
        for u in range(1, n+1):
            for v in graph[u]:
                for w in graph[v].intersection(graph[u]):
                    min_degree = min(min_degree, degree[u] + degree[v] + degree[w]  - 6)
                    graph[w].discard(u)
                graph[v].discard(u)
            
        return min_degree if min_degree != float('inf') else -1