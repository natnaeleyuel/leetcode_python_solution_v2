class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        T = int(n**0.5)

        groups = [[] for _ in range(T)]
        for l, r, k, v in queries:
            if k < T:
                groups[k].append((l, r, v))
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD

        df = [1] * (n + T)
        for k in range(1, T):
            if not groups[k]:
                continue

            df[:] = [1] * len(df)
            for l, r, v in groups[k]:
                df[l] = df[l] * v % MOD
                R = ((r - l) // k + 1) * k + l
                df[R] = df[R] * pow(v, MOD - 2, MOD) % MOD

            for i in range(k, n):
                df[i] = df[i] * df[i - k] % MOD

            for i in range(n):
                nums[i] = nums[i] * df[i] % MOD

        return reduce(xor, nums)