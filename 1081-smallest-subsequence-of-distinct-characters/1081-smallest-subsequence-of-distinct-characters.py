class Solution:
    def smallestSubsequence(self, s: str) -> str:
        cnt = [0] * 26
        vis = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        stack = []

        for ch in s:
            i = ord(ch) - 97
            cnt[i] -= 1

            if vis[i]:
                continue

            while stack and stack[-1] > ch and cnt[ord(stack[-1]) - 97]:
                vis[ord(stack.pop()) - 97] = 0

            stack.append(ch)
            vis[i] = 1

        return "".join(stack)