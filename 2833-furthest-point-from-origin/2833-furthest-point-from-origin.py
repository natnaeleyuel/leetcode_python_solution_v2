class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = 0
        r_count = 0
        _count = 0

        for mv in moves:
            if mv == "L": 
                l_count += 1
            elif mv == "R":
                r_count += 1
            else:
                _count += 1

        return _count + max(l_count, r_count) - min(l_count, r_count)