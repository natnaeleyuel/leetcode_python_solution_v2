class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = 0
        r_count = 0

        for mv in moves:
            if mv == "L": 
                l_count += 1
            if mv == "R":
                r_count += 1

        return len(moves) - 2 * min(l_count, r_count)