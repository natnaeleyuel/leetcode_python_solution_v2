class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        one_count = count.get(1, 0)
        res = one_count if one_count % 2 else one_count - 1
        count.pop(1, None)

        for num in count:
            curr = 0
            x = num
            while x in count and count[x] > 1:
                curr += 2
                x *= x

            res = max(res, curr + (1 if x in count else -1))

        return res