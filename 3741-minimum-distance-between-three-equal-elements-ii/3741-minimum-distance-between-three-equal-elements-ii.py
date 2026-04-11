class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        store = defaultdict(list)
        min_dist = float("inf")

        for i, j in enumerate(nums):
            store[j].append(i)
        
        for v, idxs in store.items():
            if len(idxs) < 3:
                continue
            else:
                i = 0
                j = 1
                k = 2

                while k < len(idxs):
                    curr_dist = abs(idxs[i] - idxs[j]) + abs(idxs[j] - idxs[k]) + abs(idxs[k] - idxs[i])
                    min_dist = min(min_dist, curr_dist)
                    i += 1
                    j += 1
                    k += 1
        
        return min_dist if min_dist != float("inf") else -1