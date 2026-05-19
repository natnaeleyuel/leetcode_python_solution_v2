class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])

        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        def can(k):
            for i in range(k, n + 1):
                for j in range(k, m + 1):

                    total = (
                        prefix[i][j]
                        - prefix[i - k][j]
                        - prefix[i][j - k]
                        + prefix[i - k][j - k]
                    )

                    if total <= threshold:
                        return True

            return False

        left = 0
        right = min(n, m)

        while left < right:
            mid = (left + right + 1) // 2

            if can(mid):
                left = mid
            else:
                right = mid - 1

        return left