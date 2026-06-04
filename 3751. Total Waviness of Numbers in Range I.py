wave_count = [0]

for n in range(1, 10 ** 5 + 1):
    s = str(n)

    if len(s) <= 2:
        wave_count.append(0)
    else:
        waves = 0

        for idx in range(1, len(s) - 1):
            l = int(s[idx - 1])
            d = int(s[idx])
            r = int(s[idx + 1])
            if d < min(l, r) or d > max(l, r):
                waves += 1
        
        wave_count.append(waves)

wave_totals = []
curr_tot = 0

for n in wave_count:
    curr_tot += n
    wave_totals.append(curr_tot)

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return wave_totals[num2] - wave_totals[num1 - 1]