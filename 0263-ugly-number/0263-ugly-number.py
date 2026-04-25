class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n == 0:
            return False 

        for i in range(1, 32):
            while n % 2 ** i == 0:
                n /= 2 ** i

        for i in range(1, 21):
            while n % 3 ** i == 0:
                n /= 3 ** i

        for i in range(1, 15):
            while n % 5 ** i == 0:
                n /= 5 ** i
        
        return n == 1