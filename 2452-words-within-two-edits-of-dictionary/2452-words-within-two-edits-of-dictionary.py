class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []

        for q in queries:
            n = len(q)
            found = False
            for d in dictionary:
                df = 0
                for i in range(n):
                    if q[i] != d[i]:
                        df += 1
            
                found = found | (df <= 2)
            
            if found: 
                res.append(q)
        
        return res
