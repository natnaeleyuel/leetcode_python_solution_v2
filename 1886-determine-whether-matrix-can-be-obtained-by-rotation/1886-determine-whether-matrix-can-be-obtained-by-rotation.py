import numpy as np
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
            
        def rotate_90_d(org_list):
            n = len(org_list)
            res = [[0] * n for _ in range(n)]
            k = n - 1
        
            for i in range(n):
                for j in range(n):
                    res[j][k] = org_list[i][j]
                
                k -= 1
            
            return res
        
        for _ in range(3):
            mat = rotate_90_d(mat)
            if mat == target:
                return True
        
        return False