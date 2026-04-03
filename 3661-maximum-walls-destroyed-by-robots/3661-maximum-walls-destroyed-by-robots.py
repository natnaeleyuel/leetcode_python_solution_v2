class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        arr = sorted(zip(robots, distance), key=lambda x: x[0])
        walls.sort()

        @lru_cache
        def dfs(i: int, next_dir: int) -> int:
            if i < 0:
                return 0

            pos, dist = arr[i]

            left = pos - dist
            if i > 0:
                prev_pos = arr[i-1][0]
                left = max(left, prev_pos + 1)
            l = bisect_left(walls, left)
            r = bisect_left(walls, pos + 1)
            destroy_left = (r - l) + dfs(i-1, 0)

            right = pos + dist
            if i + 1 < n:
                next_pos, next_dist = arr[i+1]
                if next_dir == 0:
                    right = min(right, next_pos - next_dist - 1)
                else:
                    right = min(right, next_pos - 1)
            l = bisect_left(walls, pos)
            r = bisect_left(walls, right + 1)
            destroy_right = (r - l) + dfs(i-1, 1)

            return max(destroy_left, destroy_right)

        return dfs(n-1, 1)
