class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        valid_wave_count = 0

        for num in range(num1, num2+1):
            curr_n = num
            
            if curr_n < 100:
                continue 

            prev_d = curr_n % 10
            curr_n //= 10
            curr_d = curr_n % 10
            curr_n //= 10
            next_d = curr_n % 10
            curr_n //= 10

            if (curr_d < prev_d and curr_d < next_d) or (curr_d > prev_d and curr_d > next_d):
                valid_wave_count += 1

            while True:
                if curr_n == 0:
                    break

                prev_d = curr_d
                curr_d = next_d
                next_d = curr_n % 10
                curr_n //= 10

                if (curr_d < prev_d and curr_d < next_d) or (curr_d > prev_d and curr_d > next_d):
                    valid_wave_count += 1

        return valid_wave_count




