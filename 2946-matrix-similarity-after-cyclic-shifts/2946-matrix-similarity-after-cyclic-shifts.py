class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        mat_2 = [[mat[i][j] for j in range(n)] for i in range(m)]

        if n == 1:
            return True

        for i in range(k):
            for j in range(m):
                if j % 2 == 0:
                        mat_2[j] = mat_2[j][1:] + [mat_2[j][0]]
                else:
                    mat_2[j] = [mat_2[j][-1]] + mat_2[j][:n-1]
        
        return mat == mat_2
        
