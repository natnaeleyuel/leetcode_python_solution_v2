class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = deque([0])
        far = 0

        while q:
            i = q.popleft()

            start = max(i + minJump, far)
            end = min(i + maxJump + 1, n)

            for j in range(start, end):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    q.append(j)

            far = end

        return n == 1