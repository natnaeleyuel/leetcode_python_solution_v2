class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        
        for i in range(len(cost)-3, -1, -3):
            cost[i] = 0
        
        return  sum(cost)