class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        res = []

        for q in queries:
            for d in dictionary:
                df = 0
                for i in range(n):
                    if q[i] != d[i]:
                        df += 1
                        if df > 2: break
            
                if df <= 2: 
                    res.append(q)
                    break
        
        return res
