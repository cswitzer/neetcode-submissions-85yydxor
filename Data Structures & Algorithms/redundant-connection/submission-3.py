class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0 for _ in range(n + 1)]
        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
            indegree[src] += 1
            indegree[dest] += 1

        q = deque()

        # iterate over node indices, not degree values
        for node in range(1, n + 1):
            if indegree[node] == 1:
                q.append(node)

        # pop all leaf nodes
        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        # return the last edge that participates in the cycle
        for u, v in reversed(edges):
            if indegree[u] > 0 and indegree[v] > 0:
                return [u, v]

        return []
