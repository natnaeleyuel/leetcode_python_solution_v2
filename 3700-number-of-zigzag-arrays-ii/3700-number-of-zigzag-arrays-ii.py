class Solution:
    MOD = 10**9 + 7
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        if n == 1:
            return m

        sz = 2 * m

        T = [[0] * sz for _ in range(sz)]

        for i in range(m):
            for j in range(i):
                T[i][m + j] = 1

        for i in range(m):
            for j in range(i + 1, m):
                T[m + i][j] = 1

        def matmul(A, B):
            C = [[0] * sz for _ in range(sz)]

            for i in range(sz):
                for k in range(sz):
                    if A[i][k]:
                        aik = A[i][k]

                        for j in range(sz):
                            if B[k][j]:
                                C[i][j] = (
                                    C[i][j] + aik * B[k][j]
                                ) % self.MOD

            return C

        def matpow(M, e):
            R = [[0] * sz for _ in range(sz)]

            for i in range(sz):
                R[i][i] = 1

            while e:
                if e & 1:
                    R = matmul(R, M)

                M = matmul(M, M)
                e >>= 1

            return R

        P = matpow(T, n - 1)

        start = [1] * sz

        ans = 0

        for i in range(sz):
            row = 0

            for j in range(sz):
                row = (row + P[i][j] * start[j]) % self.MOD

            ans = (ans + row) % self.MOD

        return ans