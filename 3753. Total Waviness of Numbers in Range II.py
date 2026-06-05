class Solution:
    def waveTotal(self, num):
        numstr = str(num)
        @cache
        def helper(i, minAllowed, maxAllowed, prev, bounded, firstNum):
            # returns (count, total_waviness)
            if minAllowed > maxAllowed:
                return (0, 0)
            if i == len(numstr) - 1:
                if bounded:
                    maxAllowed = min(maxAllowed, int(numstr[i]))
                if minAllowed > maxAllowed:
                    return (0, 0)
                return (maxAllowed - minAllowed + 1, 0)

            res_cnt = 0
            res_wave = 0
            if bounded:
                if int(numstr[i]) > maxAllowed:
                    bounded = False
                maxAllowed = min(maxAllowed, int(numstr[i]))
            if minAllowed > maxAllowed:
                return (0, 0)

            if firstNum:
                if i == len(numstr) - 2:
                    return (0, 0)
                if minAllowed == 0:
                    c, w = helper(i + 1, 0, 9, 0, False, True)
                    res_cnt += c
                    res_wave += w
                for j in range(max(minAllowed, 1), maxAllowed + 1):
                    bound = bounded and j == maxAllowed
                    c, w = helper(i + 1, 0, 9, j, bound, False)
                    res_cnt += c
                    res_wave += w
                return (res_cnt, res_wave)

            # j < prev (descending)
            for j in range(minAllowed, min(maxAllowed + 1, prev)):
                bound = bounded and j == maxAllowed
                # next > j = valley
                up_c, up_w = helper(i + 1, j + 1, 9, j, bound, False)
                # next <= j = continuing descent or equal
                dn_c, dn_w = helper(i + 1, 0, j, j, bound, False)
                res_cnt += up_c + dn_c
                res_wave += (up_w + up_c) + dn_w  # +1 per valley path

            # j == prev
            if prev >= minAllowed and prev <= maxAllowed:
                bound = bounded and prev == maxAllowed
                eq_c, eq_w = helper(i + 1, 0, 9, prev, bound, False)
                res_cnt += eq_c
                res_wave += eq_w

            # j > prev (ascending)
            for j in range(max(prev + 1, minAllowed), maxAllowed + 1):
                bound = bounded and j == maxAllowed
                # next < j = peak
                dn_c, dn_w = helper(i + 1, 0, j - 1, j, bound, False)
                # next >= j = continuing ascent or equal
                up_c, up_w = helper(i + 1, j, 9, j, bound, False)
                res_cnt += dn_c + up_c
                res_wave += (dn_w + dn_c) + up_w  # +1 per peak path

            return (res_cnt, res_wave)

        cnt, wave = helper(0, 0, 9, -1, True, True)
        return wave
                
            
            

        
    def totalWaviness(self, num1: int, num2: int) -> int:
        l = self.waveTotal(num1 - 1)
        r = self.waveTotal(num2)
        print(l, r)
        return r - l
        