class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = 0
        c = 0

        return moves.count("U") == moves.count("D") and moves.count("R") == moves.count("L")