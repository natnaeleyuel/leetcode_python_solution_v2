class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        prf_sum = [[grid[i][j] for j in range(n)] for i in range(m)]
    
        for i in range(m):
            for j in range(1, n):
                prf_sum[i][j] += prf_sum[i][j-1]

        hrz_prf_sum = [prf_sum[i][-1] for i in range(m)]
        hrz_suf_sum = [prf_sum[i][-1] for i in range(m)]

        for i in range(1, m):
            hrz_prf_sum[i] += hrz_prf_sum[i-1]

        for i in range(m-2, -1, -1):
            hrz_suf_sum[i] += hrz_suf_sum[i+1]

        for i in range(m - 1):
            if hrz_prf_sum[i] == hrz_suf_sum[i+1]:
                return True
       
        prf_sum = [[grid[i][j] for j in range(n)] for i in range(m)]

        for i in range(n):
            for j in range(1, m):
                prf_sum[j][i] += prf_sum[j-1][i]

        ver_prf_sum = [prf_sum[-1][i] for i in range(n)]
        ver_suf_sum = [prf_sum[-1][i] for i in range(n)]

        for i in range(1, n):
            ver_prf_sum[i] += ver_prf_sum[i-1]

        for i in range(n-2, -1, -1):
            ver_suf_sum[i] += ver_suf_sum[i+1]

        for i in range(n - 1):
            if ver_prf_sum[i] == ver_suf_sum[i+1]:
                return True

        return False