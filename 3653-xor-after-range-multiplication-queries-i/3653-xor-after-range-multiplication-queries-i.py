class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        for (l, r, k, v) in queries:
            print(l, r, k, v)
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10 ** 9 + 7)
                idx += k
        
        return reduce(xor, nums)

