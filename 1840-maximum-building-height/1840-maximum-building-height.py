class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        r = restrictions
        r.append([1, 0])
        r.sort()

        if r[-1][0] != n:
            r.append([n, n - 1])

        n = len(r)

        for i in range(1, n):
            r[i][1] = min(r[i][1], r[i - 1][1] + (r[i][0] - r[i - 1][0]))
            
        for i in range(n - 2, 0, -1):
            r[i][1] = min(r[i][1], r[i + 1][1] + (r[i + 1][0] - r[i][0]))

        res = 0
        for i in range(n - 1):
            best = ((r[i + 1][0] - r[i][0]) + r[i][1] + r[i + 1][1]) // 2
            res = max(res, best)

        return res