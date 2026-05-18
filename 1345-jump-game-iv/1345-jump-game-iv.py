class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        mp = defaultdict(list)

        for i, v in enumerate(arr):
            mp[v].append(i)

        q = deque([0])
        vis = {0}
        steps = 0
        while q:

            for _ in range(len(q)):
                i = q.popleft()
                if i == n - 1:
                    return steps

                neighbors = mp[arr[i]] + [i - 1, i + 1]
                for nxt in neighbors:
                    if 0 <= nxt < n and nxt not in vis:
                        vis.add(nxt)
                        q.append(nxt)

                mp[arr[i]].clear()

            steps += 1