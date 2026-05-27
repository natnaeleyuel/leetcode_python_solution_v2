class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_last_apr = defaultdict(int)
        upper_first_apr = defaultdict(int)

        for i, c in enumerate(word):
            if c == c.lower():
                lower_last_apr[c] = i
            if c == c.upper() and c not in upper_first_apr:
                upper_first_apr[c] = i
        
        count = 0

        for c, idx_first in upper_first_apr.items():
            if c.lower() not in lower_last_apr:
                continue
            
            idx_last = lower_last_apr[c.lower()]

            if idx_first > idx_last:
                count += 1
        
        return count
