class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)], key=lambda x: x[0])
        stack = [] 
        survivors = []  

        for pos, health, dirc, idx in robots:
            if dirc == 'R':
                stack.append([pos, health, idx])
            else:  
                while stack and health > 0:
                    top_pos, top_health, top_idx = stack[-1]
                    
                    if top_health == health:
                        stack.pop()
                        health = 0
                        break

                    elif top_health > health:
                        stack[-1][1] -= 1
                        health = 0
                        break

                    else:
                        health -= 1
                        stack.pop()
                
                if health > 0:
                    survivors.append([pos, health, idx])
        
        all_survivors = stack + survivors
        all_survivors.sort(key=lambda x: x[2])
        return [health for pos, health, idx in all_survivors]
