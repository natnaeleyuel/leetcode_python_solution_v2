class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()

        count = 0
        for i in range(len(cost)-1, -1, -1):
            if count == 2:
                count = 0
                cost[i] = 0
                continue 
            
            count += 1
        
        return  sum(cost)