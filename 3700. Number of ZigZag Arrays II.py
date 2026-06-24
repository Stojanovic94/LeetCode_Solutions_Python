class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # Store the modulo constant.
        MOD = 10**9 + 7

        # Count how many values are available in the inclusive range [l, r].
        M = r - l + 1

        # Handle length one directly.
        if n == 1:
            # Any value in the range can be chosen.
            return M % MOD

        # Handle length two directly.
        if n == 2:
            # Pick the first value freely, then pick any different second value.
            return (M % MOD) * ((M - 1) % MOD) % MOD

        # Handle length three directly when M is very large.
        if n == 3 and M > 100000:
            # Start with the first factor M.
            ans = M % MOD

            # Multiply by M - 1.
            ans = ans * ((M - 1) % MOD) % MOD

            # Multiply by 2M - 1.
            ans = ans * ((2 * M - 1) % MOD) % MOD

            # Divide by 3 using modular inverse.
            ans = ans * pow(3, MOD - 2, MOD) % MOD

            # Return the closed-form result.
            return ans

        # Use direct dynamic programming only when the table is genuinely manageable.
        if n * M <= 20_000_000 and not (M <= 300 and n > 1000):
            # Allocate upward transition states.
            up = [0] * M

            # Allocate downward transition states.
            down = [0] * M

            # Fill the base states for sequences of length two.
            for i in range(M):
                # Count ways ending at value i with the last move going upward.
                up[i] = i % MOD

                # Count ways ending at value i with the last move going downward.
                down[i] = (M - 1 - i) % MOD

            # Build answers for lengths 3 through n.
            for _ in range(3, n + 1):
                # Allocate the next upward DP array.
                next_up = [0] * M

                # Allocate the next downward DP array.
                next_down = [0] * M

                # Reset running prefix sum.
                s = 0

                # Build upward moves from previous downward moves.
                for i in range(M):
                    # All smaller previous values can move upward into i.
                    next_up[i] = s

                    # Add the current downward state for future larger positions.
                    s += down[i]

                    # Keep the running sum modulo MOD.
                    if s >= MOD:
                        s -= MOD

                # Reset running suffix sum.
                s = 0

                # Build downward moves from previous upward moves.
                for i in range(M - 1, -1, -1):
                    # All larger previous values can move downward into i.
                    next_down[i] = s

                    # Add the current upward state for future smaller positions.
                    s += up[i]

                    # Keep the running sum modulo MOD.
                    if s >= MOD:
                        s -= MOD

                # Replace old upward states with newly computed ones.
                up = next_up

                # Replace old downward states with newly computed ones.
                down = next_down

            # Add all valid arrays ending with an upward last move.
            ans = sum(up) % MOD

            # Add all valid arrays ending with a downward last move.
            ans = (ans + sum(down)) % MOD

            # Return the direct DP result.
            return ans

        # Use interpolation when n is small but M is too large for direct DP.
        if n <= 300:
            # Use n + 1 sample points for a polynomial of degree at most n.
            k = n + 1

            # Store sample answers y[1], y[2], ..., y[k].
            y = [0] * (k + 1)

            # Compute each sample answer using small direct DP.
            for sample_m in range(1, k + 1):
                # Allocate upward states for this sample size.
                up = [0] * sample_m

                # Allocate downward states for this sample size.
                down = [0] * sample_m

                # Initialize length-two states for the sample range.
                for i in range(sample_m):
                    # Smaller values can transition upward into i.
                    up[i] = i % MOD

                    # Larger values can transition downward into i.
                    down[i] = (sample_m - 1 - i) % MOD

                # Extend this sample DP up to length n.
                for _ in range(3, n + 1):
                    # Allocate next upward states.
                    next_up = [0] * sample_m

                    # Allocate next downward states.
                    next_down = [0] * sample_m

                    # Reset prefix sum for upward transitions.
                    s = 0

                    # Compute upward states using previous downward states.
                    for j in range(sample_m):
                        # Store the number of ways to rise into value j.
                        next_up[j] = s

                        # Add current downward state to the prefix.
                        s += down[j]

                        # Apply modulo to the running sum.
                        if s >= MOD:
                            s -= MOD

                    # Reset suffix sum for downward transitions.
                    s = 0

                    # Compute downward states using previous upward states.
                    for j in range(sample_m - 1, -1, -1):
                        # Store the number of ways to fall into value j.
                        next_down[j] = s

                        # Add current upward state to the suffix.
                        s += up[j]

                        # Apply modulo to the running sum.
                        if s >= MOD:
                            s -= MOD

                    # Update upward states for this sample.
                    up = next_up

                    # Update downward states for this sample.
                    down = next_down

                # Sum upward-ending sample arrays.
                total = sum(up) % MOD

                # Add downward-ending sample arrays.
                total = (total + sum(down)) % MOD

                # Store the finished sample value.
                y[sample_m] = total

            # Return directly when the real M is already sampled.
            if M <= k:
                # No interpolation is needed.
                return y[M]

            # Allocate factorial table for denominator values.
            fact = [1] * (k + 1)

            # Build factorials from 1 to k.
            for i in range(1, k + 1):
                # Store i! modulo MOD.
                fact[i] = fact[i - 1] * i % MOD

            # Allocate prefix product table.
            pref = [1] * (k + 2)

            # Build products before each interpolation index.
            for j in range(1, k + 1):
                # Multiply by M - j.
                pref[j] = pref[j - 1] * ((M - j) % MOD) % MOD

            # Allocate suffix product table.
            suff = [1] * (k + 2)

            # Build products after each interpolation index.
            for j in range(k, 0, -1):
                # Multiply by M - j.
                suff[j] = suff[j + 1] * ((M - j) % MOD) % MOD

            # Initialize interpolation answer.
            ans = 0

            # Evaluate the Lagrange interpolation sum.
            for i in range(1, k + 1):
                # Product of all M - j terms except j = i.
                num = pref[i - 1] * suff[i + 1] % MOD

                # Magnitude of denominator from left and right distances.
                den = fact[i - 1] * fact[k - i] % MOD

                # Apply sign based on how many negative factors appear.
                if (k - i) % 2 == 1:
                    # Flip denominator sign modulo MOD.
                    den = (MOD - den) % MOD

                # Start the interpolation term with y[i].
                term = y[i]

                # Multiply by numerator.
                term = term * num % MOD

                # Divide by denominator using modular inverse.
                term = term * pow(den, MOD - 2, MOD) % MOD

                # Add current basis contribution.
                ans = (ans + term) % MOD

            # Return the interpolated answer.
            return ans

        # Use recurrence jumping when M is small and n is huge.
        if M <= 300:
            # Generate enough terms to recover the recurrence.
            k = 2 * M + 5

            # Store sequence values by length.
            y = []

            # Store the length-one answer.
            y.append(M % MOD)

            # Allocate upward states.
            up = [0] * M

            # Allocate downward states.
            down = [0] * M

            # Initialize length-two DP states.
            for i in range(M):
                # Ways to end at i after an upward move.
                up[i] = i % MOD

                # Ways to end at i after a downward move.
                down[i] = (M - 1 - i) % MOD

            # Compute the length-two total.
            total = sum(up) % MOD

            # Add downward-ending states.
            total = (total + sum(down)) % MOD

            # Store the length-two answer.
            y.append(total)

            # Generate more sequence values.
            for _ in range(3, k + 1):
                # Allocate next upward states.
                next_up = [0] * M

                # Allocate next downward states.
                next_down = [0] * M

                # Reset prefix sum.
                s = 0

                # Build upward transitions.
                for i in range(M):
                    # Rising into i requires the previous value to be smaller.
                    next_up[i] = s

                    # Add current downward state into the prefix sum.
                    s += down[i]

                    # Keep the prefix sum reduced.
                    if s >= MOD:
                        s -= MOD

                # Reset suffix sum.
                s = 0

                # Build downward transitions.
                for i in range(M - 1, -1, -1):
                    # Falling into i requires the previous value to be larger.
                    next_down[i] = s

                    # Add current upward state into the suffix sum.
                    s += up[i]

                    # Keep the suffix sum reduced.
                    if s >= MOD:
                        s -= MOD

                # Move upward DP forward one length.
                up = next_up

                # Move downward DP forward one length.
                down = next_down

                # Sum upward-ending arrays for this generated length.
                total = sum(up) % MOD

                # Add downward-ending arrays for this generated length.
                total = (total + sum(down)) % MOD

                # Store this generated sequence term.
                y.append(total)

            # Initialize Berlekamp-Massey connection polynomial.
            C = [1]

            # Initialize backup polynomial.
            B = [1]

            # Store current recurrence length.
            L = 0

            # Store gap since last update.
            m = 1

            # Store last nonzero discrepancy.
            b = 1

            # Recover a linear recurrence from generated values.
            for idx in range(len(y)):
                # Start discrepancy from current sequence value.
                d = y[idx]

                # Apply current recurrence coefficients.
                for i in range(1, L + 1):
                    # Add C[i] * y[idx - i] into discrepancy.
                    d = (d + C[i] * y[idx - i]) % MOD

                # A zero discrepancy means current recurrence still fits.
                if d == 0:
                    # Increase distance from last correction.
                    m += 1

                    # Continue to the next sequence value.
                    continue

                # Save old polynomial before correction.
                old_C = C[:]

                # Compute correction multiplier.
                coef = d * pow(b, MOD - 2, MOD) % MOD

                # Make C long enough for the correction.
                if len(C) < len(B) + m:
                    # Append zeros until indices are valid.
                    C += [0] * (len(B) + m - len(C))

                # Apply correction using backup polynomial B.
                for j in range(len(B)):
                    # Shift B by m and subtract scaled version.
                    C[j + m] = (C[j + m] - coef * B[j]) % MOD

                # Check if recurrence length must increase.
                if 2 * L <= idx:
                    # Update recurrence length.
                    L = idx + 1 - L

                    # Replace backup polynomial.
                    B = old_C

                    # Store new reference discrepancy.
                    b = d

                    # Reset correction distance.
                    m = 1
                else:
                    # Keep same recurrence length and increase distance.
                    m += 1

            # Convert connection polynomial into recurrence coefficients.
            rec = [0] * (len(C) - 1)

            # Fill recurrence coefficients.
            for i in range(1, len(C)):
                # Negate connection coefficient.
                rec[i - 1] = (-C[i]) % MOD

            # Store recurrence size.
            k = len(rec)

            # Convert length n into zero-based sequence index.
            target = n - 1

            # Return directly if target was already generated.
            if target < k:
                # The stored sequence already contains the answer.
                return y[target] % MOD

            # Initialize answer polynomial as constant 1.
            ans_poly = [1] + [0] * (k - 1)

            # Initialize base polynomial representing x.
            if k == 1:
                # For degree-one recurrence, x reduces to rec[0].
                base_poly = [rec[0]]
            else:
                # Otherwise x is represented by coefficient at index one.
                base_poly = [0, 1] + [0] * (k - 2)

            # Binary exponentiation to compute x^target modulo recurrence.
            while target:
                # Multiply answer polynomial when current bit is set.
                if target & 1:
                    # Allocate raw product polynomial.
                    temp = [0] * (2 * k - 1)

                    # Multiply ans_poly and base_poly.
                    for i in range(k):
                        # Skip zero coefficients.
                        if ans_poly[i]:
                            # Scan base polynomial coefficients.
                            for j in range(k):
                                # Skip zero coefficients.
                                if base_poly[j]:
                                    # Add product into degree i + j.
                                    temp[i + j] = (temp[i + j] + ans_poly[i] * base_poly[j]) % MOD

                    # Reduce high-degree terms.
                    for deg in range(2 * k - 2, k - 1, -1):
                        # Read coefficient of current high degree.
                        coeff = temp[deg]

                        # Only reduce nonzero terms.
                        if coeff:
                            # Replace x^deg using recurrence.
                            for i in range(k):
                                # Push coefficient into lower degrees.
                                temp[deg - 1 - i] = (temp[deg - 1 - i] + coeff * rec[i]) % MOD

                    # Store reduced multiplication result.
                    ans_poly = temp[:k]

                # Allocate raw square polynomial.
                temp = [0] * (2 * k - 1)

                # Square the base polynomial.
                for i in range(k):
                    # Skip zero coefficients.
                    if base_poly[i]:
                        # Scan the second copy of base polynomial.
                        for j in range(k):
                            # Skip zero coefficients.
                            if base_poly[j]:
                                # Add square product into degree i + j.
                                temp[i + j] = (temp[i + j] + base_poly[i] * base_poly[j]) % MOD

                # Reduce high-degree square terms.
                for deg in range(2 * k - 2, k - 1, -1):
                    # Read current high-degree coefficient.
                    coeff = temp[deg]

                    # Reduce only when coefficient is nonzero.
                    if coeff:
                        # Replace this degree using recurrence coefficients.
                        for i in range(k):
                            # Push contribution into valid lower degree.
                            temp[deg - 1 - i] = (temp[deg - 1 - i] + coeff * rec[i]) % MOD

                # Store reduced square as the next base.
                base_poly = temp[:k]

                # Shift to the next binary exponent bit.
                target >>= 1

            # Initialize final answer from polynomial coefficients.
            ans = 0

            # Combine x^target coefficients with initial sequence values.
            for i in range(k):
                # Add coefficient times initial term.
                ans = (ans + ans_poly[i] * y[i]) % MOD

            # Return recurrence-jumped answer.
            return ans

        # Guard for unsupported huge-n and huge-M combinations.
        return 0