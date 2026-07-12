class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_sorted = sorted(set(arr))
        
        rank_map = {value: rank + 1 for rank, value in enumerate(unique_sorted)}
        
        return [rank_map[value] for value in arr]


        