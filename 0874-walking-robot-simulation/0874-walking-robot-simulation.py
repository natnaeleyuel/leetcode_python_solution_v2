class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obst_set = set()
        
        for r, c in obstacles:
            obst_set.add((r, c))
        
        drc = 1
        m_d = 0
        c_p = [0, 0]

        for c in commands:
            if c == -1:
                if drc != 0:
                    drc -= 1
                else:
                    drc = 3
            elif c == -2:
                if drc != 3:
                    drc += 1
                else:
                    drc = 0
            else:
                if drc == 0:
                    for _ in range(c):
                        if (c_p[0] + 1, c_p[1]) in obst_set:
                            break
                        else:
                            c_p[0] += 1
                            m_d = max(m_d, c_p[0]**2 + c_p[1]**2)
                elif drc == 1:
                    for _ in range(c):
                        if (c_p[0], c_p[1] + 1) in obst_set:
                            break
                        else:
                            c_p[1] += 1
                            m_d = max(m_d, c_p[0]**2 + c_p[1]**2)
                elif drc == 2:
                    for _ in range(c):
                        if (c_p[0] - 1, c_p[1]) in obst_set:
                            break
                        else:
                            c_p[0] -= 1
                            m_d = max(m_d, c_p[0]**2 + c_p[1]**2)
                elif drc == 3:
                    for _ in range(c):
                        if (c_p[0], c_p[1] - 1) in obst_set:
                            break
                        else:
                            c_p[1] -= 1
                            m_d = max(m_d, c_p[0]**2 + c_p[1]**2)
        
        return m_d