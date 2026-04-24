class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = Counter(moves)
        return count["_"] + max(count["L"], count["R"]) - min(count["L"], count["R"])