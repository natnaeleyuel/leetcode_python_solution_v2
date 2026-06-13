class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def compute(word: str) -> int:
            weights_sum = 0

            for c in word:
                weights_sum += weights[ord(c) - 97]
            
            return weights_sum % 26
        
        n = len(words)

        res = [""] * n

        for i in range(n):
            word = words[i]

            res[i] = chr(97 + abs(compute(word) - 25))

        return "".join(res)