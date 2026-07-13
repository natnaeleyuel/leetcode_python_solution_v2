class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []

        for l in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - l):
                x = int(s[i:i + l])
                if low <= x <= high:
                    res.append(x)

        return res