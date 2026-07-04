class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        res = float("inf")
        vis = set()

        def dfs(u):
            nonlocal res
            vis.add(u)

            for v, w in graph[u]:
                res = min(res, w)
                if v not in vis:
                    dfs(v)

        dfs(1)
        return res