class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        
        n = len(arr)
        visited = set()
        possible = False
        queue = deque([start])
        while queue:
            poped = queue.popleft()
            visited.add(poped)
            x = poped + arr[poped]
            y = poped - arr[poped]
            if x < n:
                if arr[x] == 0:
                    possible = True
                    break
                elif x not in visited:
                    queue.append(x)
                    
            if y >= 0:
                if arr[y] == 0:
                    possible = True
                    break
                elif y not in visited:
                    queue.append(y)
        
        return possible 