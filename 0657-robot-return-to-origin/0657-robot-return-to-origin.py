class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = 0
        c = 0

        for m in moves:
            if m == "U":
                r -= 1
            if m == "D":
                r += 1
            if m == "R":
                c += 1
            if m == "L":
                c -= 1

        return r == 0 and c == 0