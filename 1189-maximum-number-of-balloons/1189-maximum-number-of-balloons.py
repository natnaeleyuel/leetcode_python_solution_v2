class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)

        a_count = count["a"]
        b_count = count["b"]
        l_count = count["l"] // 2
        n_count = count["n"]
        o_count = count["o"] // 2

        return min(a_count, b_count, l_count, n_count, o_count)