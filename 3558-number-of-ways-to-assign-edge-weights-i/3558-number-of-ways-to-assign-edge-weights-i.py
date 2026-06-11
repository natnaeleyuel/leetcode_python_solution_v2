class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, p):
            depth = 0

            for v in g[u]:
                if v != p:
                    depth = max(depth, 1 + dfs(v, u))

            return depth

        m = dfs(1, 0)

        return pow(2, m - 1, MOD)