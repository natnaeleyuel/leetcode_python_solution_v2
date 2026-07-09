class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        store = [i for i in range(n)]

        for i in range(1, n):
            if nums[i]-nums[i-1] <= maxDiff: 
                store[i] = store[i-1]
        
        return [store[i] == store[j] for i,j in queries]