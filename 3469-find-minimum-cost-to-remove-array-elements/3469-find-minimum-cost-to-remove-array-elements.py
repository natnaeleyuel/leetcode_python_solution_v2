class Solution:
    def minCost(self, nums: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dp(prev: int, i: int) -> int:
            if i + 2 > n:
                return max(prev, *nums[i:]) if i < n else prev

            c, b, a = sorted((nums[i], nums[i+1], prev))

            ans = a + dp(c, i + 2)
            ans = min(ans, b + dp(a, i + 2))

            return ans

        n = len(nums)

        if n < 3:
            return max(nums)

        return dp(nums[0], 1)